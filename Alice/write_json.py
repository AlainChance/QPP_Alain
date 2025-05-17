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

# os — Miscellaneous operating system interfaces
# https://docs.python.org/3/library/os.html
import os

import json

def write_json(num_of_qubits=2, plaintext_file="Christmas_tree.png", version="V0", trace=1):

    file_size = os.path.getsize(plaintext_file)
    print(f"Plaintext file size: {file_size} bytes")

    job_trigger = int(file_size/10) + 1
    print_trigger = job_trigger

    trace = trace

    if num_of_qubits < 6:
        match num_of_qubits:
            case 2:
                num_of_bits = 448
                num_of_perm_in_pad = 56
            case 3:
                num_of_bits = 408
                num_of_perm_in_pad = 17
            case 4:
                num_of_bits = 384
                num_of_perm_in_pad = 6
            case 5:
                num_of_bits = 480
                num_of_perm_in_pad = 3
    else:
        num_of_perm_in_pad = 3
        n = 2**num_of_qubits
        num_of_bits = (n-1) * num_of_qubits * num_of_perm_in_pad * 2

    if num_of_qubits > 3:
        version = "V0"

    json_param = {
        "num_of_bits": num_of_bits,
        "num_of_qubits": num_of_qubits,
        "num_of_perm_in_pad": num_of_perm_in_pad,
        "pad_selection_key_size": 6,
        "opt_level": 1,
        "resilience_level": 1,
        "plaintext_file": plaintext_file,
        "token_file": "Token_Alain.txt",
        "trace": trace,
        "job_trigger": job_trigger,
        "print_trigger": print_trigger,
        "draw_circuit": "True",
        "do_sampler": "True",
        "version": version,
        "len_message": 12758,
        "len_ciphertext": 102064
        }
    
    # Serializing json
    json_object = json.dumps(json_param, indent=4)
 
    # Write to QPP_param.json
    with open('QPP_param.json', 'w') as json_file:
        json_file.write(json_object)

    return