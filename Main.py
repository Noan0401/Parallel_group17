import sys
import math
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
from datetime import datetime

import Monte
import Plot
import Para


print("並列なし")
start_time = datetime.now()
total = []
for i in range(10000):
    total.append(Monte.monte(i))
print(total[-1])
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

print("並列あり")
Para.Para(1)

print("並列なし")
start_time = datetime.now()
total2 = []
for i in range(10000):
    total2.append(Monte.monte2(i))
print(total2[-1][0])
end_time = datetime.now()
Plot.plot_graph(total2[-1][1],total2[-1][2],0,10000)
print('Duration: {}'.format(end_time - start_time))

print("並列あり")
Para.Para2(1,10000)
