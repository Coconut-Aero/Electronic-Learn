import numpy as np
from graph_generator import main as generator

def nand2(x, y):
    return int(not (x and y))

def nand3(x, y, z):
    return int(not (x and y and z))

def rounding(a1, a2, a3, a4):
    return nand3(nand2(a4, a4), nand2(a3, a2), nand2(a3, a1))

A4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
A3 = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])
A2 = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])
A1 = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

output = []
for a1, a2, a3, a4 in zip(A1, A2, A3, A4):
    output.append(rounding(a1, a2, a3, a4))

steps = np.arange(len(A1))
steps_extended = np.repeat(steps, 2)[1:]

A1_extended = np.repeat(A1, 2)[:-1]
A2_extended = np.repeat(A2, 2)[:-1]
A3_extended = np.repeat(A3, 2)[:-1]
A4_extended = np.repeat(A4, 2)[:-1]
output_extended = np.repeat(np.array(output), 2)[:-1]

generator(5,
          steps_extended,
          len(A1),
          "Rounding Circuit Simulation (Digital Signals)",
          "img1.png",
          A1_extended,A2_extended,A3_extended,A4_extended, output_extended,'Input A1','Input A2','Input A3', 'Input A4', 'Output')