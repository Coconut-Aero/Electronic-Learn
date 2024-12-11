import numpy as np
import share_func
from graph_generator import main as generator

def d0(last_state):
    return int((last_state != 1))

def d1(d0_last_state, d1_last_state, x_input):
    return int(not(share_func.xor2(x_input, share_func.xor2(d0_last_state, d1_last_state))))

def output(d0_last_state, d1_last_state, x_input):
    return int((d0_last_state == 1 and d1_last_state == 1 and x_input == 1)or(d0_last_state == 0 and d1_last_state == 0 and x_input == 0))

input_x = np.array([0,0,0,0,0,1,1,1,1,1])
output_q0 = []
output_q1 = []
output_z = []

for i in range(10):
    if i==0:
        output_q0.append(0)
        output_q1.append(0)
        output_z.append(0)
    elif i<=4 or i>5:
        output_q0.append(d0(output_q0[i-1]))
        output_q1.append(d1(output_q0[i-1],output_q1[i-1],input_x[i]))
        output_z.append(output(output_q0[i],output_q1[i],input_x[i]))
    elif i==5:
        output_q0.append(0)
        output_q1.append(0)
        output_z.append(d1(output_q0[i],output_q1[i],input_x[i]))


steps = np.arange(len(input_x))
steps_extended = np.repeat(steps, 2)[1:]

input_x_extended = np.repeat(input_x, 2)[1:]
output_q0_extended = np.repeat(np.array(output_q0), 2)[1:]
output_q1_extended = np.repeat(np.array(output_q1), 2)[1:]
output_z_extended = np.repeat(np.array(output_z), 2)[1:]

generator(4,
          steps_extended,
          len(input_x),
          "Counter Circuit Simulation (Digital Signals)",
          "img.png",
          input_x_extended, output_q0_extended, output_q1_extended, output_z_extended,"Input","Q0","Q1","Output")


