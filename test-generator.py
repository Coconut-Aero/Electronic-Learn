import numpy as np
from graph_generator import main as generator

A = np.array([0, 0, 0, 0, 1, 1, 1, 1])
B = np.array([0, 0, 1, 1, 0, 0, 1, 1])
C = np.array([0, 1, 0, 1, 0, 1, 0, 1])
steps = np.arange(len(A))
steps_extended = np.repeat(steps, 2)[1:]
A_extended = np.repeat(A, 2)[:-1]
B_extended = np.repeat(B, 2)[:-1]
C_extended = np.repeat(C, 2)[:-1]

generator(3,steps_extended,len(A),"Vote Circuit Simulation (Digital Signals)",A_extended,B_extended,C_extended,'Input A','Input B','Input C')