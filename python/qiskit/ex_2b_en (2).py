#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import Image, display
Image("ryoko.png", width="70")


# # Message from Dr. Ryoko
# "*Hi! I hope you now understand how the Lights Out puzzle works.<br/>The floor of the room I must cross has 3 x 3 tiles. Each tile is made of a single qubit.<br/>
# Some of these qubits fluctuate between the ground state and the excited state. <br/> I have been observing their behavior and noticed that there is a pattern - the floor can only be in either one of the four patterns as shown in each of the examples below. <br/>
# Due to decoherence, there is not enough time to play around with the switches.<br/> You need to find out which board can be cleared with three switch operations. Good luck!*"<br/>

# # Week2-B: Four-Lights Out
# In this problem, we are dealing with multiple binary data at the same time. 
# We have to determine if each of the given four Lights Out boards are solvable under the given constraints, so let's devise a quantum circuit to solve them all at the same time.
# 
# As an example, let's consider how to find a board that can be cleared with just a single switch operation from the 4 boards given below. The initial state of the 4 boards is given in the following two-dimensional array, where "0" and "1" represent "off" and "on" respectively similar to the previous learning problem:
# 
# lightsout4_ex=\[\[Board 0\],\[Board 1\],\[Board 2\],\[Board 3\]\]

# In[2]:


from IPython.display import Image, display
Image('4lightsout_ex.png')


# ## Answer Strategy
# If only one board is given, this is a decision problem.
# Using the algorithm from the first Lights Out puzzle (2A), you can solve this problem by counting the "1"s in the output.
#  
# If we are given multiple boards, there will be several approaches.
# 1. Iterate the same "one board algorithm" for each board.
# 2. Hold information for multiple boards at the same time and solve the problems in a single run (execute the algorithm once). 
# - For the rest of this document, we discuss how to use the latter approach to solve this type of problem.
# 
# First, how do we keep data for all the boards at the same time?
# 1. Naive data structures:　　9 Qubits/board * 4 boards > 32 qubits (Upper limit of ibm_qasm_simulator).
# 2. Prepare the  superposition state:   $\vert Board 0\rangle + \vert Board 1\rangle + \vert Board 2\rangle + \vert Board 3\rangle$.
#     - The circuit configuration used for state generation is non-trivial.
# 3. *qRAM* is known as one solution. 
#     - **Pros**: Intuitive implementation. 
#     - **Cons**: Computationally expensive. 
# 
# Of course you can devise and adopt other smart ways to do this.
# 
# Here, we will focus on *qRAM* and describe its configuration and implementation.

# In[3]:


# Initialization
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

# Importing Qiskit
from qiskit import IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

# Import basic plot tools
from qiskit.tools.visualization import plot_histogram


# ## qRAM: Quantum Random Access Memory
# 
# In classical computers, RAM (Random Access Memory) is a type of volatile memory that has memory addresses $j$ and stores binary data corresponding to each address $D_j$.
# 
# In the case of [qRAM](https://arxiv.org/abs/0708.1879) in a quantum computer, **address qubits $a$** have the $N$-addresses as superposition and the corresponding binary data is stored in **data qubits $d$** as a state vector.
# \\[
# \sum_{j}\frac{1}{\sqrt{N}}\vert j \rangle_{a}\vert 0 \rangle_{d}\xrightarrow{qRAM}\sum_{j}\frac{1}{\sqrt{N}}\vert j \rangle_{a}\vert D_{j} \rangle_{d}
# \\]　　
# We call the right-hand side state "qRAM" and the corresponding gate operation "qRAM operation".
# 
# Although qRAM operation requires $\mathcal{O}(N\log N)$ gates, it can be used to create superposition states of binary data intuitively.  
# 
# qRAM has previously been applied to various quantum machine learning algorithms such as the HHL algorithm. For this problem, let's apply qRAM to Grover's algorithm.

# ## Example: Find the data from qRAM
# Prepare a qRAM of $n$-addresses in which the numbers $k_0, k_1, .. , k_{n-1}$ are stored in this order.  
# Find the address in which the number $m$ is stored using Grover's algorithm.  
# - $n = 4$
# - $k = [1,2,5,7]$
# - $m = 7$
# 
# ### qRAM operation.
# Here we show a circuit example of qRAM.

# In[4]:


address = QuantumRegister(2)
data = QuantumRegister(3)
c = ClassicalRegister(5)
qc = QuantumCircuit(address,data,c)

# address preparation
qc.h([address[0],address[1]])
qc.barrier()
# address 0 -> data = 1
qc.x([address[0],address[1]])
qc.ccx(address[0],address[1],data[2])
qc.x([address[0],address[1]])
qc.barrier()
# address 1 -> data = 2
qc.x(address[0])
qc.ccx(address[0],address[1],data[1])
qc.x(address[0])
qc.barrier()
# address 2 -> data = 5
qc.x(address[1])
qc.ccx(address[0],address[1],data[2])
qc.ccx(address[0],address[1],data[0])
qc.x(address[1])
qc.barrier()
# address 3 -> data = 7
qc.ccx(address[0],address[1],data[2])
qc.ccx(address[0],address[1],data[1])
qc.ccx(address[0],address[1],data[0])
qc.barrier()


#Check the qRAM　status
qc.measure(address[0:2], c[0:2])
qc.measure(data[0:3], c[2:5])
 
# Reverse the output string.
qc = qc.reverse_bits()

#backend = provider.get_backend('ibmq_qasm_simulator')
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend=backend, shots=8000, seed_simulator=12345, backend_options={"fusion_enable":True})
#job = execute(qc, backend=backend, shots=8192)
result = job.result()
count =result.get_counts()
print(count)

qc.draw(output='mpl')


# ### qRAM Data Search
# To perform Grover's algorithm, we invert the sign of the **address qubit** containing $m$. We also need to initialize the **data qubit** by another qRAM operation before the Diffusion operation,
# 
# \begin{align*}
# \vert j \rangle_{a}\vert D_{j} \rangle_{d} \vert - \rangle_{f}
# \xrightarrow{oracle}  
# \left \{
#  \begin{array}{l}
# -\vert j \rangle_{a}\vert D_{j} \rangle_{d} \vert - \rangle_{f},  D_{j} = m\\
# \vert j \rangle_{a}\vert D_{j} \rangle_{d} \vert - \rangle_{f},  D_{j}  \neq m
#  \end{array}
#  \right.
#  \xrightarrow{qRAM}
# \left \{
#  \begin{array}{l}
# -\vert j \rangle_{a}\vert 0 \rangle_{d}\vert - \rangle_{f},  D_{j} = m \\
# \vert j \rangle_{a}\vert 0 \rangle_{d}\vert - \rangle_{f},　D_{j}\neq m
#  \end{array}
#  \right.
#  \end{align*}
#  
# where $f$ denotes the flag qubit.  
# 
# In this case, we can configure an oracle operation using the [C3X gate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.C3XGate.html#qiskit.circuit.library.C3XGate) . 
# 
# Here, we show the whole circuit for our [qRAM example](#qRAM-Example:-Find-the-data-from-qRAM).

# In[ ]:


Image('circuit_ex.png')


# ### Considerations for qRAM implementation
# In the above description we have introduced a naive *qRAM operation* circuit.
# Depending on the data structure, we can simplify the circuit by using **gate synthesis** (equivalence transformation) techniques.
# Also, some simplified gates, e.g. [RCCX](https://qiskit.org/documentation/stubs/qiskit.circuit.library.RCCXGate.html#qiskit.circuit.library.RCCXGate), may help improve your *CNOT*-saving implementation.
# 
# An example of gate synthesis is shown below.

# In[ ]:


Image('gatesynthesis_ex.png')


# ## Learning Exercise II-B
# Let's solve a 4-Lights Out problem with qRAM.  
# 
# When the initial board state lightsout4=\[\[Board 0\],\[Board 1\],\[Board 2\],\[Board 3\]\] is described by the following data, 
# determine the _binary_ number of the solvable boards in $3$ switch operations.  (ex. Board 0 → 00, 1 → 01, 2 → 10, 3 → 11)
# 
# Answer by creating a quantum circuit to solve the puzzle shown in the figure below. In the quantum circuit to be submitted, measure only the `solution` (2bit) that solves the puzzle.
# 
# To submit your solution, create a function which takes "lightsout4" as an input and returns `QuantumCircuit`.  You can choose a function name you like. Make sure it works even if you input another dataset to "lightsout4".
# 
#  **In addition, please implement the quantum circuit within 28 qubits.**
# 
# Please note that you can get the answer with the same endian as the one used in the description. You can also use the following function.
# ```python
# qc = qc.reverse_bits()
# ```

# In[ ]:


Image('4lightsout_pr.png')


# In[5]:


lightsout4=[[0,0,0, 0,1,1, 0,0,1], [0,1,0, 1,1,0, 0,0,0], [0,1,1, 1,0,0, 0,0,1], [1,0,0, 0,0,0, 1,0,1]]


# ### Hints
# - Change the oracle of [qRAM data search](#qRAM-Data-search) to an appropriate one.
# - Data storing/writing in *QRAM operation* can be performed in any order. We can reduce the number of gates by taking into account the _hamming distance_ of the address and input data.

# In[6]:


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


# In[7]:


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
    


# In[8]:


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
    


# In[9]:


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
        


# In[10]:


import itertools
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
    


# In[11]:


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
    
    for i in range(1):
        #QRAM
        qram(qc, add, inp, lightsout4)

        #U2A
        for i in range(1):
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
        for i in range(1):
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

qc = week2b_ans_func(lightsout4)    
qc.draw(output='text')


# In[12]:


from qiskit import IBMQ
provider = IBMQ.load_account()
backend = provider.get_backend("ibmq_qasm_simulator")
shots = 2048
results = execute(qc, backend=backend, shots=shots).result()
answer = results.get_counts()
print(answer)


# In[13]:


# Submission code
from qc_grader import prepare_ex2b, grade_ex2b, submit_ex2b

# Execute your circuit with following prepare_ex2b() function.
# The prepare_ex2b() function works like the execute() function with only QuantumCircuit as an argument.
job  =  prepare_ex2b(week2b_ans_func)

result = job.result()
count = result.get_counts()
original_problem_set_counts = count[0]

original_problem_set_counts
# The bit string with the highest number of observations is treated as the solution.


# In[14]:


# Check your answer by executing following code.
# The quantum cost of the QuantumCircuit is obtained as the score. The quantum cost is related to rank only in the third week.
grade_ex2b(job)


# In[ ]:


# Submit your results by executing following code. You can submit as many times as you like during the period. 
submit_ex2b(job)

