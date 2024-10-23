from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def nand2(x, y):
    return int(not (x and y))

def nand4(x, y, z, m):
    return int(not (x and y and z and m))

def vote(x, y, z):
    nand_xy = nand2(x, y)
    nand_xz = nand2(x, z)
    nand_yz = nand2(y, z)
    output = nand4(nand_xy, nand_xz, nand_yz, 1)
    return int(output)

A = np.array([0, 0, 0, 0, 1, 1, 1, 1])
B = np.array([0, 0, 1, 1, 0, 0, 1, 1])
C = np.array([0, 1, 0, 1, 0, 1, 0, 1])

vote_output = []

steps = np.arange(len(A))
steps_extended = np.repeat(steps, 2)[1:]

for a, b, c in zip(A, B, C):
    vote_result = vote(a, b, c)  # Rename the variable here
    vote_output.append(vote_result)

A_extended = np.repeat(A, 2)[:-1]
B_extended = np.repeat(B, 2)[:-1]
C_extended = np.repeat(C, 2)[:-1]
vote_extended = np.repeat(np.array(vote_output), 2)[:-1]

fig, axs = plt.subplots(4, 1, figsize=(8, 10))

axs[0].step(steps_extended, A_extended, where='post', label="Input A", marker='o', color='red')
axs[0].set_title('Input A')
axs[0].set_ylabel('Digital Signal')

axs[1].step(steps_extended, B_extended, where='post', label="Input B", marker='o', color='blue')
axs[1].set_title('Input B')
axs[1].set_ylabel('Digital Signal')

axs[2].step(steps_extended, C_extended, where='post', label="Input C", marker='o', color='green')
axs[2].set_title('Input C')
axs[2].set_ylabel('Digital Signal')

axs[3].step(steps_extended, vote_extended, where='post', label="Vote Result", marker='o', color='orange')
axs[3].set_title('Vote Result')
axs[3].set_xlabel('Simulation Steps')
axs[3].set_ylabel('Digital Signal')

for ax in axs:
    ax.set_xticks(np.arange(len(A)))
    ax.set_xticklabels(np.arange(1, len(A) + 1))

plt.suptitle('Vote Circuit Simulation (Digital Signals)', fontsize=16)

plt.tight_layout()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
plt.annotate(f"Author: XiaoYi Zero\nGenerated on: {current_time}\nSoftware: Python & Matplotlib & KiCAD",
             xy=(0.99, 0.01), xycoords='figure fraction', ha='right', va='bottom', fontsize=10)

plt.show()
