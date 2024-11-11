import numpy as np
from graph_generator import main as generator

class DFlipFlop:
    def __init__(self):
        self.Q = 0
        self.not_Q = 1

    def set_input(self, D, clock):
        if clock == 1:  # 只有在时钟信号为1时才更新状态
            if D == 0:
                self.Q = 0
                self.not_Q = 1
            elif D == 1:
                self.Q = 1
                self.not_Q = 0

    def output(self):
        return self.Q, self.not_Q

# 定义需要的颜色函数
def colors(i):
    color_list = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan']
    return color_list[i % len(color_list)]

# 准备输入数据
def simulate_d_flipflop():
    D_values = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
    clock_values = [1, 1, 0, 1, 1, 0, 1, 0, 1, 1]
    Q_values = []
    not_Q_values = []

    d_ff = DFlipFlop()
    for D, clock in zip(D_values, clock_values):
        d_ff.set_input(D, clock)
        Q, not_Q = d_ff.output()
        Q_values.append(Q)
        not_Q_values.append(not_Q)

    return D_values, clock_values, Q_values, not_Q_values

# 获取模拟数据
D_values, clock_values, Q_values, not_Q_values = simulate_d_flipflop()

# 设置参数
count = 4  # 信号的数量（D, Clock, Q, not_Q）
steps_extended = np.arange(0, 10)  # 时间步长
lens = 10  # 时间步数
suptitle = "Clocked D Flip-Flop Simulation"

# 调用 main 函数生成波形图
generator(count, steps_extended, lens, suptitle,"img1.png",
     D_values, clock_values, Q_values, not_Q_values,
     "D Input", "Clock Input", "Q Output", "not_Q Output")
