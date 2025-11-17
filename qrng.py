"""
Quantum Random Number Generator Using Bell States
"""

#Importing necessary libraries
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

sim = AerSimulator()
random_bits = ""

for _ in range(50):
    #Creating 2-qubit quantum circuit
    qc1 = QuantumCircuit(2,2)

    #Creating Bell state
    qc1.h(0)
    qc1.cx(0,1)

    #Measuring both qubits
    qc1.measure([0,1],[0,1])
    
    #Execute the simulator
    result = sim.run(qc1, shots=1).result()

    #Read the output either '00' or '11'
    bits = list(result.get_counts().keys())[0]

    #Convert to classical bit
    if bits == "00":
        random_bits += "0"
    else:
        random_bits += "1"
        
print(len(random_bits))    
print(list(random_bits))
