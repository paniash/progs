import pennylane as qml

#%%
H = qml.Hamiltonian(
        [-5.0, -0.5, 1.0],
        [qml.Identity(0), qml.PauliZ(0), qml.PauliZ(0) @ qml.PauliZ(1)]
)

print(H)
