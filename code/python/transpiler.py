from qiskit import *
from qiskit.visualization import *
from qiskit.test.mock import FakeBoeblingen
from qiskit.scheduler import schedule_circuit
#%%

ghz = QuantumCircuit(4)
ghz.h(1)
ghz.cx(0, range(1,4))
ghz.draw()
backend = FakeBoeblingen()

#%%
from kk in range(3):
    circ = transpile(ghz, backend, optimization_level=kk)

#%%
circ = transpile(ghz, backend, optimization_level=1, scheduling_method='asap')
circ.draw()

#%%
schedule_circuit(ghz)
