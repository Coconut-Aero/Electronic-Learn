import numpy as np
from graph_generator import main as generator

class RSFlipFlop:
    def __init__(self):
        self.Q = 0
        self.not_Q = 1

    def set_input(self, R, S):
        if R == 0 and S == 0:
            # No change condition
            pass
        elif R == 0 and S == 1:
            # Set condition
            self.Q = 1
            self.not_Q = 0
        elif R == 1 and S == 0:
            # Reset condition
            self.Q = 0
            self.not_Q = 1
        elif R == 1 and S == 1:
            # Invalid condition (R = 1, S = 1)
            print("Invalid condition! Both R and S cannot be 1.")

    def output(self):
        return self.Q, self.not_Q


def simulate_rs_flipflop():
    rs_ff = RSFlipFlop()
    R_values = [0, 1, 0, 0, 1, 0, 1, 1, 0, 0]
    S_values = [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    Q_values = []
    not_Q_values = []

    for R, S in zip(R_values, S_values):
        rs_ff.set_input(R, S)
        Q, not_Q = rs_ff.output()
        Q_values.append(Q)
        not_Q_values.append(not_Q)

    return R_values, S_values, Q_values, not_Q_values

R_values, S_values, Q_values, not_Q_values = simulate_rs_flipflop()

count = 4  # 信号的数量（D, Clock, Q, not_Q）
steps_extended = np.arange(0, 10)  # 时间步长
lens = 10  # 时间步数
suptitle = "Basic R-S Flip-Flop Simulation"

generator(count, steps_extended, lens, suptitle,"img2.png",
     R_values, S_values, Q_values, not_Q_values,
     "R Input", "S Input", "Q Output", "not_Q Output")