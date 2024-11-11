import numpy as np
from graph_generator import main as generator

class ClockedRSFlipFlop:
    def __init__(self):
        self.Q = 0
        self.not_Q = 1

    def set_input(self, R, S, clock):
        if clock == 1:
            if R == 0 and S == 0:
                pass
            elif R == 0 and S == 1:
                self.Q = 1
                self.not_Q = 0
            elif R == 1 and S == 0:
                self.Q = 0
                self.not_Q = 1
            elif R == 1 and S == 1:
                print("Invalid state")

    def output(self):
        return self.Q, self.not_Q

# 准备模拟数据
def simulate_clocked_rs_flipflop():
    clocked_rs_ff = ClockedRSFlipFlop()
    R_values = [0, 1, 0, 0, 1, 0, 1, 1, 0, 0]
    S_values = [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    clock_values = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
    Q_values = []
    not_Q_values = []

    for R, S, clock in zip(R_values, S_values, clock_values):
        clocked_rs_ff.set_input(R, S, clock)
        Q, not_Q = clocked_rs_ff.output()
        Q_values.append(Q)
        not_Q_values.append(not_Q)

    return R_values, S_values, clock_values, Q_values, not_Q_values

R_values, S_values, clock_values, Q_values, not_Q_values = simulate_clocked_rs_flipflop()

count = 5  # 信号的数量（D, Clock, Q, not_Q）
steps_extended = np.arange(0, 10)  # 时间步长
lens = 10  # 时间步数
suptitle = "Clocked R-S Flip-Flop Simulation"

generator(count, steps_extended, lens, suptitle,"img3.png",
     R_values, S_values, clock_values, Q_values, not_Q_values,
     "R Input", "S Input","Clock Input", "Q Output", "not_Q Output")