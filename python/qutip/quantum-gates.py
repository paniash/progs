from qutip import *
from qutip.qip.operations import *
from qutip.qip.circuit import QubitCircuit, Gate

#%%
qcirc = QubitCircuit(2, reverse_states=False)
qcirc.add_gate("CSIGN", controls=[0], targets=[1])
qcirc.png
