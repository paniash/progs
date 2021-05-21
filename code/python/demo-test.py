import xacc
import numpy as np

qpu = xacc.getAccelerator('qpp')
ham = xacc.getObservable('pauli', '-5.0 - 0.5 Z0 + 1.0 Z0Z1')
nbQubits = 2
steps = 1
buffer = xacc.qalloc(nbQubits)
nbTotalParams = 4
# The optimizer: nlopt
opt = xacc.getOptimizer('nlopt', { 'initial-parameters': np.random.rand(nbTotalParams)} )

# Create the QAOA algorithm
qaoa = xacc.getAlgorithm('QAOA', {
                        'accelerator': qpu,
                        'observable': ham,
                        'optimizer': opt,
                        'steps': steps,
                        'parameter-scheme': 'Extend'})
# Run
result = qaoa.execute(buffer)
print('Min value = ', buffer.getInformation('opt-val'))
print('Opt-params = ', buffer.getInformation('opt-params'))

# Get the circuit
qaoa_ansatz_std = xacc.createComposite('qaoa')
qaoa_ansatz_std.expand({'nbQubits': nbQubits, 'nbSteps': steps, 'cost-ham': ham,
    'parameter-scheme':'Extend'})
print('Extend parameterized QAOA circuit:')
print(qaoa_ansatz_std)
