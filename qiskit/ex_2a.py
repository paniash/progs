# The starting pattern is represented by this list of numbers.
# Please use it as an input for your solution.
lights = [0, 1, 1, 1, 0, 0, 1, 1, 1]

from qiskit import *

def map_board(lights, qc, tile):
    for i in range(len(lights)):
        if lights[i] == 1:
            qc.x(tile[i])

    return qc

def initialize(lights, qc, flip, tile, oracle):
    map_board(lights, qc, tile)

    qc.h(flip[:])
    qc.x(oracle[0])
    qc.h(oracle[0])

def flip_tile(qc, flip, tile):
    qc.cx(flip[0], tile[0])
    qc.cx(flip[0], tile[1])
    qc.cx(flip[0], tile[3])

    qc.cx(flip[1], tile[0])
    qc.cx(flip[1], tile[1])
    qc.cx(flip[1], tile[2])
    qc.cx(flip[1], tile[4])

    qc.cx(flip[2], tile[1])
    qc.cx(flip[2], tile[2])
    qc.cx(flip[2], tile[5])

    qc.cx(flip[3], tile[0])
    qc.cx(flip[3], tile[3])
    qc.cx(flip[3], tile[4])
    qc.cx(flip[3], tile[6])

    qc.cx(flip[4], tile[1])
    qc.cx(flip[4], tile[3])
    qc.cx(flip[4], tile[4])
    qc.cx(flip[4], tile[5])
    qc.cx(flip[4], tile[7])

    qc.cx(flip[5], tile[2])
    qc.cx(flip[5], tile[4])
    qc.cx(flip[5], tile[5])
    qc.cx(flip[5], tile[8])

    qc.cx(flip[6], tile[3])
    qc.cx(flip[6], tile[6])
    qc.cx(flip[6], tile[7])

    qc.cx(flip[7], tile[4])
    qc.cx(flip[7], tile[6])
    qc.cx(flip[7], tile[7])
    qc.cx(flip[7], tile[8])

    qc.cx(flip[8], tile[5])
    qc.cx(flip[8], tile[7])
    qc.cx(flip[8], tile[8])

def all_zero(qc, tile, oracle):
    qc.x(tile[0:9])
    qc.mct(tile[0:9], oracle[0])
    qc.x(tile[0:9])


def week2a_ans_func(lights):
    ##### build your quantum circuit here
    tile = QuantumRegister(9)
    flip = QuantumRegister(9)
    oracle = QuantumRegister(1)
    result = ClassicalRegister(9)
    qc = QuantumCircuit(flip, tile, oracle, result)

    initialize(lights, qc, flip, tile, oracle)
    qc.barrier()

    for i in range(18):
        flip_tile(qc, flip, tile)
        qc.barrier()

        all_zero(qc, tile, oracle)
        qc.barrier()

        flip_tile(qc, flip, tile)

        # diffusion
        qc.h(flip)
        qc.x(flip)
        qc.h(flip[8])
        qc.mct(flip[0:8], flip[8])
        qc.h(flip[8])
        qc.x(flip)
        qc.h(flip)
        qc.barrier()

    # uncompute
    qc.h(oracle[0])
    qc.x(oracle[0])
    qc.barrier()

    # measurement
    qc.measure(flip, result)
    qc.barrier()
    qc = qc.reverse_bits()

    #####  In addition, please make it a function that can solve the problem even with different inputs (lights). We do validation with different inputs.

    return qc
