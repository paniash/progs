from qiskit import *
import itertools


#%%
lightsout4=[[1, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0]]

#%%
def qram(qc,add,inp,lightsout4):

    # address 0 -> board = 0
    qc.x([add[0],add[1]])
    for i in range(9):
        if lightsout4[0][i]==1:
            qc.ccx(add[0],add[1],inp[i])
    qc.x([add[0],add[1]])

    # address 1 -> board = 1
    qc.x(add[0])
    for i in range(9):
        if lightsout4[1][i]==1:
            qc.ccx(add[0],add[1],inp[i])
    qc.x(add[0])

    # address 2 -> board = 2
    qc.x(add[1])
    for i in range(9):
        if lightsout4[2][i]==1:
            qc.ccx(add[0],add[1],inp[i])
    qc.x(add[1])

    # address 3 -> board = 3
    for i in range(9):
        if lightsout4[3][i]==1:
            qc.ccx(add[0],add[1],inp[i])

#%%
def diffuser_pre(qc, out, ancilla):
    # Apply transformation |s> -> |00..0> (H-gates)
    for i in range(9):
        qc.h(out[i])
    # Apply transformation |00..0> -> |11..1> (X-gates)
    for i in range(9):
        qc.x(out[i])
    # Do multi-controlled-Z gate
    qc.h(out[8])
    qc.mct(out[:8], out[8],  ancilla, mode='basic')  # multi-controlled-toffoli
    qc.h(out[8])
    # Apply transformation |11..1> -> |00..0>
    for i in range(9):
        qc.x(out[i])
    # Apply transformation |00..0> -> |s>
    for i in range(9):
        qc.h(out[i])
    # We will return the diffuser as a gate

#%%
def diffuser_end(qc, end, ancilla):
    # Apply transformation |s> -> |00..0> (H-gates)
    for i in range(2):
        qc.h(end[i])
    # Apply transformation |00..0> -> |11..1> (X-gates)
    for i in range(2):
        qc.x(end[i])
    # Do multi-controlled-Z gate
    qc.h(end[1])
    qc.mct(end[:1], end[1], ancilla, mode='basic')  # multi-controlled-toffoli
    qc.h(end[1])
    # Apply transformation |11..1> -> |00..0>
    for i in range(2):
        qc.x(end[i])
    # Apply transformation |00..0> -> |s>
    for i in range(2):
        qc.h(end[i])
    # We will return the diffuser as a gate

#%%
def pre_oracle(qc,inp,out,oracle, ancilla):
    cx_map = [[0,0],[0,1],[0,3],[1,0],[1,1],[1,2],[1,4],
             [2,1],[2,2],[2,5],[3,0],[3,3],[3,4],[3,6],
             [4,1],[4,3],[4,4],[4,5],[4,7],
             [5,2],[5,4],[5,5],[5,8],[6,3],[6,6],[6,7],
             [7,4],[7,6],[7,7],[7,8],[8,5],[8,7],[8,8]]

    #apply the switching conditions
    for i in cx_map:
        qc.cx(out[i[0]],inp[i[1]])

    for i in range(9):
        qc.x(inp[i])

    qc.mct(inp[:], oracle[0],  ancilla, mode='basic')

    #uncompute
    for i in range(9):
        qc.x(inp[i])

    for i in cx_map:
        qc.cx(out[i[0]],inp[i[1]])

#%%
def three(qc, out, ancilla, oracle):
    lst = range(9)

    #MCT 8 control
    c8x_comb = list(itertools.combinations(lst, 8))
    for i in (c8x_comb):
        c8x_control = []
        for j in i:
            c8x_control.append(out[j])
        qc.mct(c8x_control, ancilla[0], ancilla[1:], mode='basic')

    #MCT 4 control
    c4x_comb = list(itertools.combinations(lst, 4))
    for i in (c4x_comb):
        c4x_control = []
        for j in i:
            c4x_control.append(out[j])
        qc.mct(c4x_control, ancilla[1], ancilla[2:], mode='basic')

#%%
def week2b_ans_func(lightsout4):
    ##### Build your cirucuit here
    out = QuantumRegister(9, name='sol')
    add = QuantumRegister(2, name='add')
    inp = QuantumRegister(9, name='lights')
    oracle = QuantumRegister(1, name='oracle')
    ancilla = QuantumRegister(7, name='ancilla')
    cr = ClassicalRegister(2)
    qc = QuantumCircuit(out, add, inp, oracle, ancilla, cr)

    #initialization
    qc.h(out)
    qc.x(oracle)
    qc.h(oracle)
    qc.h(add)

    for i in range(2):
        #QRAM
        qram(qc, add, inp, lightsout4)

        #U2A
        for i in range(6):
            pre_oracle(qc, inp, out, oracle, ancilla)
            diffuser_pre(qc, out, ancilla)

        #counter
        three(qc, out, ancilla, oracle)
        #OR gate
        qc.cx(ancilla[0],ancilla[2])
        qc.cx(ancilla[1],ancilla[2])
        qc.ccx(ancilla[0], ancilla[1], ancilla[2])
        #flip 2
        qc.x(ancilla[2])
        qc.cx(ancilla[2],oracle[0])
        qc.x(ancilla[2])
        #uncompute
        qc.ccx(ancilla[0], ancilla[1], ancilla[2])
        qc.cx(ancilla[1],ancilla[2])
        qc.cx(ancilla[0],ancilla[2])
        three(qc, out, ancilla, oracle)

        #U2A
        for i in range(6):
            diffuser_pre(qc, out, ancilla)
            pre_oracle(qc, inp, out, oracle, ancilla)

        #QRAM
        qram(qc, add, inp, lightsout4)


        diffuser_end(qc, add, ancilla)

    qc.h(oracle)
    qc.x(oracle)
    qc.measure(add, cr)
    qc = qc.reverse_bits()


    ####  In addition, please make sure your function can solve the problem with different inputs (lightout4). We will cross validate with different inputs.

    return qc

#%%
qc = week2b_ans_func(lightsout4)
qc.draw(output='text')

#%%
backend = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend).result().get_counts()
print(counts)
