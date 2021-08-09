import math
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def monte(n):
    N_in = 0
    N_out = 0
    N = n+1
    ran_x = random.rand(N) #Xの乱数
    ran_y = random.rand(N) #Yの乱数
    ran_point = np.hypot(ran_x,ran_y) #X^2 + Y^2の平方根

    for i in ran_point:
        if i <= 1:
            N_in += 1
        else:
            N_out += 1

    Pie = N_in/N*4 #パイの近似式
    return Pie


def monte2(n):
    N_in = 0
    N_out = 0
    N = n+1
    ran_x = random.rand(N) #Xの乱数
    ran_y = random.rand(N) #Yの乱数
    ran_point = np.hypot(ran_x,ran_y) #X^2 + Y^2の平方根

    for i in ran_point:
        if i <= 1:
            N_in += 1
        else:
            N_out += 1

    Pie = N_in/N*4 #パイの近似式
    return [Pie, ran_x ,ran_y]