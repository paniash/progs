from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor

#%%
def diffuser(nqbits):
    qc = QuantumCircuit(nqbits)
    for qubit in range(nqbits):
        qc.h(qubit)

    for qubit in range(nqbits):
        qc.x(qubit)

    qc.h(nqbits-1)
    qc.mct(list(range(nqbits-1)), nqbits-1)
    qc.h(nqbits-1)

    for qubit in range(nqbits):
        qc.x(qubit)

    for qubit in range(nqbits):
        qc.h(qubit)

    U_s = qc.to_gate()
    U_s.name = "$U_s$"

    return U_s

#%%
clause_list = [[0,1], [0,2], [1,3], [2,3]]

#%%
def XOR(qc, a, b, output):
    qc.cx(a, output)
    qc.cx(b, output)

#%%
in_qubits = QuantumRegister(2, name='input')
out_qubit = QuantumRegister(1, name='output')
qc = QuantumCircuit(in_qubits, out_qubit)
XOR(qc, in_qubits[0], in_qubits[1], out_qubit)
qc.draw()

#%% Do the same for the entire clause list
var_qubits = QuantumRegister(4, name='v')
clause_qubits = QuantumRegister(4, name='c')
output_qubit = QuantumRegister(1, name='out')
cbits = ClassicalRegister(4, name='cbits')
qc = QuantumCircuit(var_qubits, clause_qubits, output_qubit, cbits)

def sudoku(qc, clause_list, clause_qubits, cbits):
    i = 0
    for clause in clause_list:
        XOR(qc, clause[0], clause[1], clause_qubits[i])
        i += 1

    qc.mct(clause_qubits, output_qubit)

    i = 0
    for clause in clause_list:
        XOR(qc, clause[0], clause[1], clause_qubits[i])
        i += 1

sudoku(qc, clause_list, clause_qubits, cbits)
qc.draw()

#%%
var_qubits = QuantumRegister(4, name='v')
clause_qubits = QuantumRegister(4, name='c')
output_qubit = QuantumRegister(1, name='out')
cbits = ClassicalRegister(4, name='cbits')
qc = QuantumCircuit(var_qubits, clause_qubits, output_qubit, cbits)

qc.initialize([1,-1]/np.sqrt(2), output_qubit)

qc.h(var_qubits)
qc.barrier()

sudoku(qc, clause_list, clause_qubits, cbits)
qc.barrier()
qc.append(diffuser(4), [0,1,2,3])

sudoku(qc, clause_list, clause_qubits, cbits)
qc.barrier()
qc.append(diffuser(4), [0,1,2,3])

qc.measure(var_qubits, cbits)
qc.draw()

#%%
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
plot_histogram(result.get_counts())
