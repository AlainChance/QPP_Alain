#--------------------------------------------------------------------------------
# Quantum Permutation Pad with Qiskit Runtime by Alain Chancé

## MIT License

# Copyright (c) 2022 Alain Chancé

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#--------------------------------------------------------------------------------

# This version features communications using JSON-RPC 2.0 over HTTP.
#
# The new Jupyter notebook Bob_agent.ipynb must be run first to start a receiver agent
# which functions as a uvicorn server and receives a file using:
# * 🛰️ FastAPI on the server (Remote Agent)
# * 📡 requests module on the client
# * 📦 File content encoded in Base64
# * 🌐 JSON-RPC 2.0 over HTTP
#
# Alice Jupyter notebook instantiates a SenderAgent and sends three files to Bob receiver agent with the send_file method using:
# * 📡 requests module
# * 📦 File content encoded in Base64
# * 🌐 JSON-RPC 2.0 over HTTP
#
# Last Bob Jupyter notebook process the files received from Alice sender agent.

## Documentation
#
# uvicorn, https://www.uvicorn.org/
# 
# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
# https://fastapi.tiangolo.com/
#
# A2A leverages JSON-RPC 2.0 as the data exchange format for communication between a Client and a Remote Agent.
# https://google.github.io/A2A/#/documentation?id=agent-to-agent-communication
#
# JS# ON-RPC 2.0 Specification, https://www.jsonrpc.org/specification
#
# Welcome to jsonrpcserver’s documentation!
# https://www.jsonrpcserver.com/en/stable/examples.html#fastapi
#
# os — Miscellaneous operating system interfaces
# https://docs.python.org/3/library/os.html
import os
import json

# shutil — High-level file operations
# https://docs.python.org/3/library/shutil.html
import shutil

# Import QPP_Alain
from QPP_Alain import QPP

from write_json import write_json

# Prompt for a filename
while True:
    plaintext_file = input("Enter plaintext filename (.txt or .png or .jpg): ").strip()
    if plaintext_file.lower().endswith((".txt", ".png", ".jpg")):
        print("You entered: ", plaintext_file)
        if os.path.isfile(plaintext_file):
            break
        else:
            print("Missing plaintext file: ", plaintext_file)    
    else:
        print("Invalid file type. Please enter a .txt or .png or .jpg file.")

# Prompt for an integer, with basic validation
while True:
    try:
        num_of_qubits = int(input("Enter number of qubits between 2 and 9: "))
        print("You entered: ", num_of_qubits)
        if num_of_qubits >= 2 and num_of_qubits <= 9:
            break
    except ValueError:
        print("Please enter a valid integer between 2 and 9")

# Prompt for version 0 or 1
while True:
    try:
        v = int(input("Enter version 0 (n qubits) or 1 (2**n qubits which only uses swap gates): "))
        print("You entered: ", v)
        if v == 0 or v == 1:
            break
    except ValueError:
        print("Please enter a valid integer 0 or 1")

if v == 1 and num_of_qubits > 4:
    v = 0
    print("Reset version to 0 when number of qubits > 4")

# Prompt for trace level 0 or 1
while True:
    try:
        trace = int(input("Enter trace level 0 or 1: "))
        print("You entered: ", trace)
        if trace == 0 or trace == 1:
            break
    except ValueError:
        print("Please enter a valid integer 0 or 1")

# Prompt for classical simulation or AerSimulator method='statevector'
while True:
    try:
        user_int = int(input("Enter 0 for classical simulation or 1 for Qiskit Runtime Sampler or AerSimulator method='statevector'"))
        print("You entered: ", user_int)
        if user_int == 0:
            do_sampler="False"
        elif user_int == 1:
            do_sampler="True"
        if user_int == 0 or user_int == 1:
            break
    except ValueError:
        print("Please enter a valid integer 0 or 1")

# Prompt for macimum number of permutations in pad when a Token file exists
max_num_of_perm = 0
if os.path.isfile("Token.txt"):
    while True:
        try:
            max_num_of_perm = int(input("Enter maximum number of permutations in pad between 0 (no maximum) and 56: "))
            print("You entered: ", max_num_of_perm)
            if max_num_of_perm >= 0 and max_num_of_perm <= 56:
                break
        except ValueError:
            print("Please enter a valid integer between 0 and 56")

# Write json file
write_json(num_of_qubits=num_of_qubits, plaintext_file=plaintext_file, version="V"+str(v), trace=trace, do_sampler=do_sampler, max_num_of_perm=max_num_of_perm)

QPP_param_file = "QPP_param.json"
if os.path.isfile(QPP_param_file):
    with open(QPP_param_file) as json_file:
        json_param = json.load(json_file)
else:
    raise RuntimeError("Missing QPP_param.json file")

# Create an instance of the QPP class
Alice_QPP = QPP("QPP_param")

# Convert plaintext file into a bitstring message
message = Alice_QPP.file_to_bitstring()

# Encrypt bitstring message
ciphertext = Alice_QPP.encrypt(message=message)

# Convert the ciphertext into bytes and save it into a binary file
Alice_QPP.ciphertext_to_binary(ciphertext=ciphertext)

# Create Alice agent
from sender_agent import SenderAgent
server_url="http://127.0.0.1:8000/rpc"
alice_agent = SenderAgent()
response_dict = {}

plaintext_file = json_param['plaintext_file']
Secret_key_file = "Secret_key_" + str(num_of_qubits) + "-qubits_" + plaintext_file[:-3] + "txt"
ciphertext_file = "ciphertext_" + plaintext_file[:-3] + "bin"
trace_file = "Trace_" + str(num_of_qubits) + "-qubits_" + plaintext_file[:-3] + "txt"

# Simulate transmission of secret key over a secure channel
response_dict = alice_agent.send_file(filename=Secret_key_file, server_url=server_url)

# Simulate transmission of json parameter file
response_dict = alice_agent.send_file(filename=QPP_param_file, server_url=server_url)

# Simulate transmission of ciphertext file
response_dict = alice_agent.send_file(filename=ciphertext_file, server_url=server_url)

print("\n\033[1mDo a File Save of this notebook\033[0m\n")

# Prompt the user
while True:
    response = input("Do you want to save the content of the Alice directory? (y/n): ").strip().lower()
    if response in ['y', 'yes']:
        print("You chose Yes.")
        Alice_dir = "../QPP_" + str(num_of_qubits) + "_qubits/" + plaintext_file[:-4] + "/Alice"
        print(f"Alice_dir: {Alice_dir}")
        os.makedirs(Alice_dir, exist_ok=True)
        shutil.copy(plaintext_file, Alice_dir)
        shutil.copy(Secret_key_file, Alice_dir)
        shutil.copy(ciphertext_file, Alice_dir)
        shutil.copy(trace_file, Alice_dir)
        shutil.copy("QPP_Alain.py", Alice_dir)
        shutil.copy("sender_agent.py", Alice_dir)
        shutil.copy("QPP_Alice.py", Alice_dir)
        shutil.copy("QPP_param.json", Alice_dir)
        shutil.copy("QPP_Alice.ipynb", Alice_dir)
        shutil.copy("Alice_agent.ipynb", Alice_dir)
        shutil.copy("Write_json.ipynb", Alice_dir)
        shutil.copy("write_json.py", Alice_dir)
        break
    elif response in ['n', 'no']:
        print("You chose No.")
        break
    else:
        print("Please enter 'y' or 'n'.")