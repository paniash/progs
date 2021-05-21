from qutip import *
from collections import namedtuple

#%%
z = np.array([0,0,1])
mu = np.array([0,1,1]) / np.sqrt(2)

bloch = Bloch()
bloch.zlabel=("z", "")
bloch.add_vectors([z, mu])
bloch.show()


#%% Stern Gerlach experiment
Direction = namedtuple("Direction", ["theta", "phi"])

def random_direction():
    r = 0
    while r == 0:
        x, y, z = np.random.normal(0, 1, 3)
        r = np.sqrt(x**2 + y**2 + z**2)
    phi = np.arctan2(y, x)
    theta = np.arccos(z/r)

    return Direction(theta=theta, phi=phi)

#%%
def classical_state(d):
    x = np.sin(d.theta) * np.cos(d.phi)
    y = np.sin(d.theta) * np.sin(d.phi)
    z = np.cos(d.theta)

    return np.array([x,y,z])

#%%
classical_up = np.array([0,0,1])

def classical_spin(c):
    return classical_up.dot(c)

#%%
def classical_stern_gerlach(n):
    directions = [random_direction() for _ in range(n)]
    atoms = [classical_state(d) for d in directions]
    spins = [classical_spin(c) for c in atoms]

    return atoms, spins

#%%
def plot_classical_results(atoms, spins):
    fig = plt.figure(figsize=(18.0, 8.0))
    fig.suptitle("Stern-Gerlach experiment: Classical outcome", fontsize="xx-large")

    ax1 = plt.subplot(1, 2, 1, projection='3d')
    ax2 = plt.subplot(1,2,2)

    b = Bloch(fig=fig, axes=ax1)
    b.vector_width = 1
    b.vector_color = ["#ff{:x}0ff".format(i, i) for i in range(10)]
    b.zlabel = ["$z$", ""]
    b.add_vectors(atoms)
    b.render(fig=fig, axes=ax1)

    ax2.hist(spins)
    ax2.set_xlabel("Z-component of spin")
    ax2.set_ylabel("# of atoms")

#%%
atoms, spins = classical_stern_gerlach(100)
plot_classical_results(atoms, spins)

#%%
def plot_real_vs_actual(spins):
    fig = plt.figure(figsize=(18.0, 8.0))
    fig.suptitle("Stern-Gerlach Experiment: Real vs Actual", fontsize="xx-large")

    ax1 = plt.subplot(1,2,1)
    ax2 = plt.subplot(1,2,2)

    ax1.hist([np.random.choice([1,-1]) for _ in spins])
    ax1.set_xlabel("Z-component of spin")
    ax1.set_ylabel("# of atoms")

    ax2.hist(spins)
    ax2.set_xlabel("Z-component of spin")
    ax2.set_ylabel("# of atoms")

#%%
plot_real_vs_actual(spins)

#%%
class ClassicalBit:
    def __init__(self, outcome):
        self.outcome = outcome

b0 = heads = ClassicalBit(outcome=0)
b1 = tails = ClassicalBit(outcome=1)

def measure_cbit(cbit):
    return cbit.outcome

print("State:\n", b0)
print("Outcome:\n", measure_cbit(b0))

#%% Quantum case
b0 = ket("0")
b1 = ket("1")

print("State:\n", b1)

#%%
def measure_qbit(qbit):
    if qbit == ket('0'):
        return 0
    if qbit == ket('1'):
        return 1
    raise NotImplementedError("No clue yet. :)")

print("Outcome:", measure_qbit(b1))

#%% The case of superposition
def plot_real_a_b():
    fig = plt.figure(figsize=(18.0, 8.0))
    fig.suptitle("Probabilities: Real $a$ and $b$", fontsize="xx-large")

    ax = plt.subplot(1,1,1)

    ax.plot([0,1], [1,0])
    ax.set_xlabel("$a$")
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylabel("$b$")
    ax.set_ylim(-0.5, 1.5)

#%%
plot_real_a_b()

#%%
b = Bloch()
up = ket("0")
down = ket("1")
x = (up + down).unit()
z = up
y = (up + (0 + 1j) * down).unit()
b.add_states([x, y, z])
b.show()

#%%
def plot_bloch(fig, ax, title, states, color_template):
    b = Bloch(fig=fig, axes=ax)
    ax.set_title(title, y=-0.01)
    b.vector_wisth = 1
    b.vector_color = [color_template.format(i * 10) for i in range(len(states))]
    b.add_states(states)
    b.render(fig=fig, axes=ax)


#%%
def plot_multi_blochs(plots):
    fig = plt.figure(figsize=(18.0, 8.0))
    fig.suptitle("Bloch Sphere", fontsize="xx-large")
    n = len(plots)
    axes = [plt.subplot(1, n, i+1, projection='3d') for i in range(n)]
    for i, (title, states, color_template) in enumerate(plots):
        plot_bloch(fig, axes[i], title, states, color_template)

#%%
up = ket('0')
down = ket('1')

magnitude_circle = [
        (a*up + np.sqrt(1-a**2) * down)
        for a in np.linspace(0, 1, 20)
        ]

angular_circle = [
        (np.sqrt(0.5) * up + np.sqrt(0.5) * down * np.exp(1j*theta))
        for theta in np.linspace(0, 2*np.pi, 20)
        ]

#%%
plot_multi_blochs([
    ["Changing relative magnitude", magnitude_circle, "#ff{:02x}ff"],
    ["Changing relative angle", angular_circle, "#{:02x}ffff"],
    ])

#%%
def measure_qbit(qbit):
    a = qbit.full()[0][0]
    b = qbit.full()[1][0]
    if np.random.random() <= np.abs(a) ** 2:
        return 0
    else:
        return 1

#%%
a = (1 + 0j) / np.sqrt(2)
b = (0 + 1j) / np.sqrt(2)
qbit = a * ket('0') + b * ket('1')

print("State:\n", qbit)
print("Outcome:", measure_qbit(qbit))

#%%
iterations = [i for i in range(200)]
measurement = [measure_qbit(qbit) for _ in iterations]

# fig = plt.figure(figsize=(18.0, 8.0))
fig, ax = plt.subplots()
ax.hist(iterations)
