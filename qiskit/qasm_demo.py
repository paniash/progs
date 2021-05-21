from qiskit import *

cr = ClassicalRegister(4, "c")
qr = QuantumRegister(4, "q")
qc = QuantumCircuit(qr, cr)

qc.h([3,2,1,0])
qc.z(3)
qc.cx(2,3)
qc.h([2,1,0])

qc.measure([0,1,2], [0,1,2])
print(qc.qasm())
