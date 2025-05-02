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
Bob_QPP = QPP(QPP_param_file="QPP_param")

# Read ciphertext binary file and extract the content to be transformed into a binary string
ciphertext = Bob_QPP.binary_to_ciphertext()

# Decrypt the ciphertext
decrypted_message = Bob_QPP.decrypt(ciphertext=ciphertext)

# Convert the decrypted message and save it into the decrypted file
Bob_QPP.bitstring_to_file(decrypted_message=decrypted_message)