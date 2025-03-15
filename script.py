import math

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# M -> [m_1, m_2, m_3, ... ]
# A_i = [A_m1, A_m2, A_m3, ... ] / 256 so that it is between 1 and 0
# |q_i> = cos((pi/2) * A_i)|0> + sin((pi/2) * A_i)|1>
# receiver sees 0s and 1s
# divides #0 / #shots
# reverses the equation for |0>
# estimates M

def encrypt(message: str):
    """Encrypting the message"""
    qc = QuantumCircuit(len(message), len(message))

    for i, char in enumerate(message):
        A_i = ord(char) / 256
        a = math.cos((math.pi / 2) * A_i)
        b = math.sin((math.pi / 2) * A_i)

        # Initialize qubit state
        qc.initialize([a, b], i)

    qc.measure(range(len(message)), range(len(message)))

    return qc


def decrypt(qc, shots=5000):
    """Decrypt the message"""
    simulator = Aer.get_backend('aer_simulator')
    transpiled_qc = transpile(qc, simulator)
    result = simulator.run(transpiled_qc, shots=shots).result()

    counts = result.get_counts()
    num_qubits = len(qc.qubits)

    recovered_message = ""

    for qubit in range(num_qubits):
        # Count how many times '0' was measured at this qubit position
        zeros = sum(v for k, v in counts.items() if k[num_qubits - qubit - 1] == '0')
        prob_0 = zeros / shots

        # Reversing the calculation to estimate the original value
        estimated_A = (math.acos(math.sqrt(prob_0)) * 2 / math.pi) * 256

        # trying to minimise the number of steps
        if estimated_A == 256:
            recovered_message += "Ā"
        elif estimated_A == 0:
            recovered_message += " "
        elif estimated_A % 1 > 0.4:
            recovered_message += chr(math.ceil(estimated_A))
        else:
            recovered_message += chr(math.floor(estimated_A))

    # for qubit in range(num_qubits):
    #     # Count how many times '0' was measured at this qubit position
    #     ones = sum(v for k, v in counts.items() if k[num_qubits - qubit - 1] == '1')
    #     prob_1 = ones / shots
    #
    #     # Reversing the calculation to estimate the original value
    #     estimated_A = (math.asin(math.sqrt(prob_1)) * 2 / math.pi) * 256
    #     recovered_message += chr(round(estimated_A))

    return recovered_message


# Testing
message = "kevin"
qc = encrypt(message)
print("Encrypted Quantum Circuit:")
print(qc)

decrypted_message = decrypt(qc)
print("Decrypted message:", decrypted_message + ".")

for char in message:
    print(ord(char))
for char in decrypted_message:
    print(ord(char))

print(chr(256))
