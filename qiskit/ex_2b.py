from qiskit import *
provider = IBMQ.load_account()

#%% ##################################################
lightsout4=[[1, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0]]


#%%
def qram_encoder(qc, address, tile, fliplightsout4):
    address = QuantumRegister(2, name='addr')
    tile = QuantumRegister(9, name='tile')
    flip = QuantumRegister(9, name='flip')
    oracle = QuantumRegister(1, name='orc')
    c = ClassicalRegister(2)
    qc = QuantumCircuit(address, tile, oracle, c)

    # address preparation
    qc.h(address[:])
    qc.h(flip[:])
    qc.x(oracle[0])
    qc.h(oracle[0])
    qc.barrier()

    # address 0 -> tile = lightsout4[0]
    qc.x([address[0],address[1]])
    for i in range(len(lightsout4[0])):
        if lightsout4[0][i] == 1:
            qc.ccx(address[0],address[1],tile[i])

    qc.x([address[0],address[1]])
    qc.barrier()

    # address 1 -> tile = lightsout4[1]
    qc.x(address[0])
    for i in range(len(lightsout4[1])):
        if lightsout4[0][i] == 1:
            qc.ccx(address[0],address[1],tile[i])
    qc.x(address[0])
    qc.barrier()

    # address 2 -> tile = lightsout4[2]
    qc.x(address[1])
    for i in range(len(lightsout4[2])):
        if lightsout4[0][i] == 1:
            qc.ccx(address[0],address[1],tile[i])
    qc.x(address[1])
    qc.barrier()

    # address 3 -> tile = lightsout4[3]
    for i in range(len(lightsout4[3])):
        if lightsout4[0][i] == 1:
            qc.ccx(address[0],address[1],tile[i])
    qc.barrier()

    # flip marked board (oracle)

    # address 3 -> tile = lightsout4[3]
    for i in range(len(lightsout4[3])):
        if lightsout4[0][i] == 1:
            qc.ccx(address[0],address[1],tile[i])
    qc.barrier()


    # address 2 -> tile = lightsout4[2]
    qc.x(address[1])
    for i in range(len(lightsout4[2])):
        if lightsout4[0][i] == 1:
            qc.ccx(address[0],address[1],tile[i])
    qc.x(address[1])
    qc.barrier()


    # address 1 -> tile = lightsout4[1]
    qc.x(address[0])
    for i in range(len(lightsout4[1])):
        if lightsout4[0][i] == 1:
            qc.ccx(address[0],address[1],tile[i])
    qc.x(address[0])
    qc.barrier()


    # address 0 -> tile = lightsout4[0]
    qc.x([address[0],address[1]])
    for i in range(len(lightsout4[0])):
        if lightsout4[0][i] == 1:
            qc.ccx(address[0],address[1],tile[i])

    qc.x([address[0],address[1]])
    qc.barrier()

    # diffusion
    qc.h(address[:2])
    qc.x(address[:2])
    qc.h(address[1])
    qc.cx(address[0], address[1])
    qc.h(address[1])
    qc.x(address[:2])
    qc.h(address[:2])


    # Check the qRAM　status
    qc.measure(address[0:2], c[0:2])

    # Reverse the output string.
    # qc = qc.reverse_bits()

    return qc


#%%
#backend = provider.get_backend('ibmq_qasm_simulator')
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend=backend, shots=8000, seed_simulator=12345, backend_options={"fusion_enable":True})
#job = execute(qc, backend=backend, shots=8192)
result = job.result()
count = result.get_counts()
print(count)
