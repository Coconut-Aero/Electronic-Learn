from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

def nand4(x, y, z, m):
    return int(not (x and y and z and m))

def ls74138(x, y, z, data):
    res = x * 4 + y * 2 + z * 1
    return int(not res==data)

A = np.array([0, 0, 0, 0, 1, 1, 1, 1])
B = np.array([0, 0, 1, 1, 0, 0, 1, 1])
C = np.array([0, 1, 0, 1, 0, 1, 0, 1])
Si = []
Ci = []

steps = np.arange(len(A))
steps_extended = np.repeat(steps, 2)[1:]

for a, b, c in zip(A, B, C):
    Si_Result = nand4(ls74138(a, b, c, 1),ls74138(a, b, c, 2),ls74138(a, b, c, 4),ls74138(a, b, c, 7))
    Ci_Result = nand4(ls74138(a, b, c, 3), ls74138(a, b, c, 5), ls74138(a, b, c, 6), ls74138(a, b, c, 7))
    Si.append(Si_Result)
    Ci.append(Ci_Result)

A_extended = np.repeat(A, 2)[:-1]
B_extended = np.repeat(B, 2)[:-1]
C_extended = np.repeat(C, 2)[:-1]
Si_extended = np.repeat(np.array(Si), 2)[:-1]
Ci_extended = np.repeat(np.array(Ci), 2)[:-1]

fig, axs = plt.subplots(5, 1, figsize=(8, 10))

axs[0].step(steps_extended, A_extended, where='post', label="Input A", marker='o', color='red')
axs[0].set_title('Input A')
axs[0].set_ylabel('Digital Signal')

axs[1].step(steps_extended, B_extended, where='post', label="Input B", marker='o', color='blue')
axs[1].set_title('Input B')
axs[1].set_ylabel('Digital Signal')

axs[2].step(steps_extended, C_extended, where='post', label="Input C", marker='o', color='green')
axs[2].set_title('Input Ci-1')
axs[2].set_ylabel('Digital Signal')

axs[3].step(steps_extended, Si_extended, where='post', label="Output Si", marker='o', color='orange')
axs[3].set_title('Output Si')
axs[3].set_ylabel('Digital Signal')

axs[4].step(steps_extended, Ci_extended, where='post', label="Output Ci", marker='o', color='purple')
axs[4].set_title('Output Ci')
axs[4].set_ylabel('Digital Signal')

for ax in axs:
    ax.set_xticks(np.arange(len(A)))
    ax.set_xticklabels(np.arange(1, len(A) + 1))

plt.suptitle('All Adder Circuit Simulation (Digital Signals)', fontsize=16)

plt.tight_layout()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
plt.annotate(f"Author: XiaoYi Zero\nGenerated on: {current_time}",
             xy=(0.01, 0.96), xycoords='figure fraction', ha='left', va='top', fontsize=10)
plt.annotate(f"Software: Python & Matplotlib & KiCAD",
             xy=(0.99, 0.95), xycoords='figure fraction', ha='right', va='top', fontsize=10)

plt.show()