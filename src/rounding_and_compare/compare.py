import numpy as np
from graph_generator import main as generator

def nand2(x, y):
    return int(not (x and y))

def int_not(x):
    return int(not x)

def compare(a1, a2, b1, b2):
    return nand2(nand2(a2, int_not(b2)),nand2(a1, int_not(b1)))

A2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
A1 = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])
B2 = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])
B1 = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

output = []
for a2, a1, b2, b1 in zip(A2, A1, B2, B1):
    output.append(compare(a1, a2, b1, b2))

steps = np.arange(len(A1))
steps_extended = np.repeat(steps, 2)[1:]

A2_extended = np.repeat(A2, 2)[:-1]
A1_extended = np.repeat(A1, 2)[:-1]
B2_extended = np.repeat(B2, 2)[:-1]
B1_extended = np.repeat(B1, 2)[:-1]
output_extended = np.repeat(np.array(output), 2)[:-1]

generator(5,
          steps_extended,
          len(A1),
          "Compare Circuit Simulation (Digital Signals)",
          "img2.png",
          A2_extended,A1_extended,B2_extended,B1_extended, output_extended,'Input A2','Input A1','Input B2', 'Input B1', 'Output')