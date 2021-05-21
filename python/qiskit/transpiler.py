from qiskit import *
from qiskit.compiler import transpile
from qiskit.transpiler import PassManager, passes
from qiskit.transpiler.passes import Unroller

#%%
qc = QuantumCircuit(3)
qc.ccx(0,1,2)
qc.draw()

#%%
pass_ = Unroller(['u1', 'u2', 'u3', 'cx'])
pm = PassManager(pass_)
new_circ = pm.run(qc)
new_circ.draw()

#%%
[pass_ for pass_ in dir(passes) if pass_[0].isupper()]
