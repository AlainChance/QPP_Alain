# QPP-Alain
Jupyter notebooks for QPP implementations from 2 to 8 qubits with a JSON-RPC 2.0 file exchange.

This repository contains companion Jupyter notebooks for Quantum Permutation Pad (QPP) implementations with Qiskit Runtime and Qiskit AerSimulator ranging from 2 to 8 qubits, serving as illustrations for the paper: Chancé, A. (2024). Quantum Permutation Pad with Qiskit Runtime. In: Femmam, S., Lorenz, P. (eds). ICCNT 2022. Springer, Cham. https://doi.org/10.1007/978-3-031-59619-3_12

Check out a recording of Alain's speech at the 12th Edition of the ICCCAS in Singapore, May 5–7, 2023, 
- on YouTube: https://www.youtube.com/watch?v=aUnWFgz-vio
- or on Bilibili: https://www.bilibili.com/video/BV1rw411r7jR/

Conference website: www.icccas.org
Randy Kuang's LinkedIn profile: https://www.linkedin.com/in/randy-kuang-05150510/
Michel Barbeau's profile: https://www.linkedin.com/in/michel-barbeau-464906291/ and https://carleton.ca/scs/people/michel-barbeau/

This version V5 features communications using JSON-RPC 2.0 over HTTP.

The new Jupyter notebook Bob_agent.ipynb must be run first to start a receiver agent which functions as a uvicorn server and receives a file using:
* 🛰️ FastAPI on the server (Remote Agent)
* 📡 requests module on the client
* 📦 File content encoded in Base64
* 🌐 JSON-RPC 2.0 over HTTP

Then Alice Jupyter notebook QPP_Alice.ipynb runs Python program QPP_Alice.py which encrypts a text or an image file and sends three files to Bob receiver agent with the send_file method using:
* 📡 requests module
* 📦 File content encoded in Base64
* 🌐 JSON-RPC 2.0 over HTTP

Finally, Bob Jupyter notebook QPP_Bob.ipynb runs Python program QPP_Bob.py which decrypts the text or the image file received from Alice using the Json parameter file and the secret key file.

These Jupyter notebooks work with Python 3.12 and the following Qiskit versions:
- Qiskit v1.3, Qiskit runtime 0.34, Qiskit Aer 0.16
- Qiskit v2.0, Qiskit runtime 0.37, Qiskit Aer 0.17

Please refer to the Qiskit documentation in section References below.

Since these Jupyter notebooks use Qiskit AerSimulator, no token file is required to run them with the option 'do_sampler = "True"' specified in the json parameter file.

The first cell of each of these companion jupyter notebooks contains the following: 
- MIT license
- Abstract
- Credit: Kuang, R., Perepechaenko
- Rights and permissions
- Adaptations made by Alain Chancé
  * Summary of updates V5
  * Summary of updates V4
  * Summary of updates V3
  * Summary of updates V2
  * Summary of updates V1      

## References

[1] Kuang, Randy. Quantum Permutation Pad for Quantum Secure Symmetric and Asymmetric Cryptography. Vol. 2, no. 1, Academia Quantum, 2025. https://doi.org/10.20935/AcadQuant7457 

[2] I. Burge, M. T. Mai and M. Barbeau, "A Permutation Dispatch Circuit Design for Quantum Permutation Pad Symmetric Encryption," 2024 13th International Conference on Communications, Circuits and Systems (ICCCAS), Xiamen, China, 2024, pp. 35-40, doi: 10.1109/ICCCAS62034.2024.10652827.

[3] Chancé, A. (2024). Quantum Permutation Pad with Qiskit Runtime. In: Femmam, S., Lorenz, P. (eds) Recent Advances in Communication Networks and Embedded Systems. ICCNT 2022. Lecture Notes on Data Engineering and Communications Technologies, vol 205. Springer, Cham. https://doi.org/10.1007/978-3-031-59619-3_12 

[4] Kuang, R., Barbeau, M. Quantum permutation pad for universal quantum-safe cryptography. Quantum Inf Process 21, 211 (2022). https://doi.org/10.1007/s11128-022-03557-y

[5] R. Kuang and N. Bettenburg, 'Shannon perfect secrecy in a discrete Hilbert space', in Proc. IEEE Int. Conf. Quantum Comput. Eng. (QCE), Oct. 2020, pp. 249-255, doi: 10.1109/QCE49297.2020.00039

[6] Kuang, R., Perepechaenko, M. Quantum encryption with quantum permutation pad in IBMQ systems. EPJ Quantum Technol. 9, 26 (2022). https://doi.org/10.1140/epjqt/s40507-022-00145-y

[7] Qiskit Runtime overview, IBM Quantum, https://cloud.ibm.com/docs/quantum-computing?topic=quantum-computing-overview

[8] QiskitRuntimeService, https://docs.quantum.ibm.com/api/qiskit-ibm-runtime/qiskit_ibm_runtime.QiskitRuntimeService#qiskitruntimeservice

[9] Qiskit v2.0 migration guide, https://docs.quantum.ibm.com/migration-guides/qiskit-2.0

[10] Qiskit Aer documentation, https://qiskit.github.io/qiskit-aer/

[11] Qiskit Aer 0.16.1, Getting started, https://qiskit.github.io/qiskit-aer/getting_started.html

[12] Qiskit Aer 0.16.1, Simulators, https://qiskit.github.io/qiskit-aer/tutorials/1_aersimulator.html

[13] Migrate from cloud simulators to local simulators, https://docs.quantum.ibm.com/migration-guides/local-simulators#aersimulator

#ICCCAS #ResearchPaper #QuantumSecurity #Quantropi #Y2Q #technology #cryptography #quantumcryptography #Cybersecurity #permutations #Qiskit #JSONRPC
