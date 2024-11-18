import numpy as np
from graph_generator import main as generator
from share_func import  ls74138
from share_func import  nand4

A = np.array([0, 0, 0, 0, 1, 1, 1, 1])
B = np.array([0, 0, 1, 1, 0, 0, 1, 1])
Gi_1 = np.array([0, 1, 0, 1, 0, 1, 0, 1])
Di = []
Gi = []

steps = np.arange(len(A))
steps_extended = np.repeat(steps, 2)[1:]

for a, b, gi_1 in zip(A, B, Gi_1):
    Di.append(nand4(ls74138(a, b, gi_1, 1),ls74138(a, b, gi_1, 2),ls74138(a, b, gi_1, 4),ls74138(a, b, gi_1, 7)))
    Gi.append(nand4(ls74138(a, b, gi_1, 1),ls74138(a, b, gi_1, 2),ls74138(a, b, gi_1, 3),ls74138(a, b, gi_1, 7)))

A_extended = np.repeat(A, 2)[:-1]
B_extended = np.repeat(B, 2)[:-1]
Gi_1_extended = np.repeat(Gi_1, 2)[:-1]
Di_extended = np.repeat(Di, 2)[:-1]
Gi_extended = np.repeat(Gi, 2)[:-1]

count = 5  # 信号的数量（D, Clock, Q, not_Q）
lens = 8  # 时间步数
suptitle = "Subtractor Simulation"

generator(count, steps_extended, lens, suptitle,"img.png",
     A_extended, B_extended, Gi_1_extended, Di_extended, Gi_extended,
     "A Input", "B Input", "Gi-1 Input", "Di Output", "Gi Output")