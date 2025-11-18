from qiskit import QuantumCircuit                      #Importing necessary libraries
from qiskit_aer import AerSimulator
import random

sim = AerSimulator()

def quant_random_int(n_qubits=4):                            #Defining a function to generate random integers
    qc = QuantumCircuit(n_qubits)                               #Creating a quantum circuit
    qc.h(range(n_qubits))                                           #Applying all the qubits in superposition
    qc.measure_all()                                                     #Measuring all the qubits
    num = sim.run(qc)                                                           #Send the circuit to AerSimulator
    result = num.result()                                                           #Wait for the result
    count = result.get_counts()                                                          #Get the measurements                
    bitstring = list(count.keys())[0]                                      #Extract the bitstring(as bits)
    print("The generated and extracted 4-bit: ",bitstring)
    return int(bitstring,2)                                              #Convert the bitstring(binary) into integer

for _ in range(10):                                                  #Call the function 10 times and print 10 quantum generated random integers
    print("The random number generated : ",quant_random_int())
