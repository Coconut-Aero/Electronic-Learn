from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

A = np.array([1, 0, 0, 0, 0])
B = np.array([0, 1, 0, 0, 0])
C = np.array([0, 0, 1, 0, 0])
D = np.array([0, 0, 0, 1, 0])
output = np.array([1, 2, 3, 4, 0])
clk = np.array(["lock", "lock", "lock", "lock", "unlock"])
clr = np.array([0, 0, 0, 0, 1])

time = np.arange(len(A))

fig, axs = plt.subplots(7, 1, figsize=(10, 14), sharex=True)

# 绘制各个信号
axs[0].plot(time, A, drawstyle='steps-post', marker='o', label="Signal A", color='tab:blue')
axs[0].set_title("Signal A")
axs[0].set_ylim(-0.2, 1.2)
axs[0].set_yticks([0, 1])

axs[1].plot(time, B, drawstyle='steps-post', marker='o', label="Signal B", color='tab:orange')
axs[1].set_title("Signal B")
axs[1].set_ylim(-0.2, 1.2)
axs[1].set_yticks([0, 1])

axs[2].plot(time, C, drawstyle='steps-post', marker='o', label="Signal C", color='tab:green')
axs[2].set_title("Signal C")
axs[2].set_ylim(-0.2, 1.2)
axs[2].set_yticks([0, 1])

axs[3].plot(time, D, drawstyle='steps-post', marker='o', label="Signal D", color='tab:red')
axs[3].set_title("Signal D")
axs[3].set_ylim(-0.2, 1.2)
axs[3].set_yticks([0, 1])

axs[4].plot(time, output, drawstyle='steps-post', marker='o', label="Output Signal", color='tab:purple')
axs[4].set_title("Output Signal")
axs[4].set_ylim(-0.2, 4.2)
axs[4].set_yticks([0, 1, 2, 3, 4])

clk_values = [1 if c == "lock" else 0 for c in clk]
axs[5].plot(time, clk_values, drawstyle='steps-post', marker='o', label="Clock", color='tab:brown')
axs[5].set_title("Clock")
axs[5].set_ylim(-0.2, 1.2)
axs[5].set_yticks([0, 1])
axs[5].set_yticklabels(['unlock', 'lock'])

axs[6].plot(time, clr, drawstyle='steps-post', marker='o', label="Clear", color='tab:cyan')
axs[6].set_title("Clear Signal")
axs[6].set_ylim(-0.2, 1.2)
axs[6].set_yticks([0, 1])
axs[6].set_yticklabels(['Inactive', 'Active'])

for ax in axs:
    ax.set_xticks(np.arange(len(A)))  # X 轴刻度在 0 到 len(A) 之间
    ax.set_xticklabels(np.arange(1, len(A) + 1))  # 从 1 到 len(A) 的刻度标签
    ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)  # 显示 X 轴刻度标签

plt.suptitle("Race-Answer Circuit Simulation (Digital Signals)", fontsize=16)
plt.tight_layout()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
plt.annotate(f"Author: XiaoYi Zero\nGenerated on: {current_time}",
                 xy=(0.01, 0.97), xycoords='figure fraction', ha='left', va='top', fontsize=10)
plt.annotate(f"Software: Python & Matplotlib & KiCAD",
                 xy=(0.99, 0.96), xycoords='figure fraction', ha='right', va='top', fontsize=10)

plt.savefig("img.png", format="png")

plt.show()
