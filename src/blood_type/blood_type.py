from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

def choose_blood_type(a, b, c, d):
    if a == 0 and b == 0 :
        return 1
    elif a == 0 and b == 1 :
        return d
    elif a == 1 and b == 0 :
        return c
    else:
        return (c == 1) and (d == 1)

A = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
B = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])
C = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])
D = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

output = []

steps = np.arange(len(A))
steps_extended = np.repeat(steps, 2)[1:]

for a, b, c, d in zip(A, B, C, D):
    output_result = choose_blood_type(a, b, c, d)
    output.append(output_result)

A_extended = np.repeat(A, 2)[:-1]
B_extended = np.repeat(B, 2)[:-1]
C_extended = np.repeat(C, 2)[:-1]
D_extended = np.repeat(D, 2)[:-1]
output_extended = np.repeat(np.array(output), 2)[:-1]

fig, axs = plt.subplots(5, 1, figsize=(8, 10))

axs[0].step(steps_extended, A_extended, where='post', label="Input A", marker='o', color='red')
axs[0].set_title('Input A')
axs[0].set_ylabel('Digital Signal')

axs[1].step(steps_extended, B_extended, where='post', label="Input B", marker='o', color='blue')
axs[1].set_title('Input B')
axs[1].set_ylabel('Digital Signal')

axs[2].step(steps_extended, C_extended, where='post', label="Input C", marker='o', color='green')
axs[2].set_title('Input C')
axs[2].set_ylabel('Digital Signal')

axs[3].step(steps_extended, D_extended, where='post', label="Input D", marker='o', color='purple')
axs[3].set_title('Input D')
axs[3].set_ylabel('Digital Signal')

axs[4].step(steps_extended, output_extended, where='post', label="Blood Test Result", marker='o', color='orange')
axs[4].set_title('Blood Test Result')
axs[4].set_xlabel('Simulation Steps')
axs[4].set_ylabel('Digital Signal')

for ax in axs:
    ax.set_xticks(np.arange(len(A)))
    ax.set_xticklabels(np.arange(1, len(A) + 1))

plt.suptitle('Blood Test Circuit Simulation (Digital Signals)', fontsize=16)

plt.tight_layout()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
plt.annotate(f"Author: XiaoYi Zero\nGenerated on: {current_time}",
             xy=(0.01, 0.96), xycoords='figure fraction', ha='left', va='top', fontsize=10)
plt.annotate(f"Software: Python & Matplotlib & KiCAD",
             xy=(0.99, 0.95), xycoords='figure fraction', ha='right', va='top', fontsize=10)

plt.show()