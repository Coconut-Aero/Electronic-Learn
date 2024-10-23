from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

def half_adder(x, y):
    s = x ^ y 
    c = x & y
    return s, c

A = np.array([0, 0, 1, 1])
B = np.array([0, 1, 0, 1])

sum_output = []
carry_output = []

for a, b in zip(A, B):
    sum_, carry = half_adder(a, b)
    sum_output.append(sum_)
    carry_output.append(carry)

steps = np.arange(len(A))
steps_extended = np.repeat(steps, 2)[1:]

A_extended = np.repeat(A, 2)[:-1]
B_extended = np.repeat(B, 2)[:-1]
sum_extended = np.repeat(sum_output, 2)[:-1]
carry_extended = np.repeat(carry_output, 2)[:-1]

fig, axs = plt.subplots(4, 1, figsize=(8, 10))


axs[0].step(steps_extended, A_extended, where='post', label="Input A", marker='o', color='red')
axs[0].set_title('Input A')
axs[0].set_ylabel('Digital Signal')

axs[1].step(steps_extended, B_extended, where='post', label="Input B", marker='o', color='blue')
axs[1].set_title('Input B')
axs[1].set_ylabel('Digital Signal')

axs[2].step(steps_extended, sum_extended, where='post', label="Sum (A XOR B)", marker='o', color='green')
axs[2].set_title('Sum (A XOR B)')
axs[2].set_ylabel('Digital Signal')

axs[3].step(steps_extended, carry_extended, where='post', label="Carry (A AND B)", marker='o', color='orange')
axs[3].set_title('Carry (A AND B)')
axs[3].set_xlabel('Simulation Steps')
axs[3].set_ylabel('Digital Signal')


for ax in axs:
    ax.set_xticks(np.arange(len(A)))
    ax.set_xticklabels(np.arange(1, len(A) + 1))

plt.suptitle('Half Adder Simulation (Digital Signals)', fontsize=16)

plt.tight_layout()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
plt.annotate(f"Author: XiaoYi Zero\nGenerated on: {current_time}\nSoftware: Python & Matplotlib & KiCAD",
             xy=(0.99, 0.01), xycoords='figure fraction', ha='right', va='bottom', fontsize=10)

plt.show()
