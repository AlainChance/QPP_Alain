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

# Import QPP_Alain
from QPP_Alain import QPP

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

# Simulate transmission of secret key over a secure channel
plaintext_file = Alice_QPP.json_param['plaintext_file']
num_of_qubits = Alice_QPP.json_param['num_of_qubits']
filename = "Secret_key_" + str(num_of_qubits) + "-qubits_" + plaintext_file[:-3] + "txt"
response_dict = alice_agent.send_file(filename=filename, server_url=server_url)

# Simulate transmission of json parameter file
filename = "QPP_param.json"
response_dict = alice_agent.send_file(filename=filename, server_url=server_url)

# Simulate transmission of ciphertext file
filename = "ciphertext_" + plaintext_file[:-3] + "bin"
response_dict = alice_agent.send_file(filename=filename, server_url=server_url)