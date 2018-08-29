import pickle
import math
import numpy as np
import matplotlib.pyplot as plt 

with open("times_220.txt", "rb") as times_220_file:
	times_220 = np.array(pickle.load(times_220_file))

with open("steps_220.txt", "rb") as steps_220_file:
	steps_220 = np.array(pickle.load(steps_220_file))

with open("times_260.txt", "rb") as times_260_file:
	times_260 = np.array(pickle.load(times_260_file))

with open("steps_260.txt", "rb") as steps_260_file:
	steps_260 = np.array(pickle.load(steps_260_file))

with open("times_160.txt", "rb") as times_160_file:
	times_160 = np.array(pickle.load(times_160_file))

with open("steps_160.txt", "rb") as steps_160_file:
	steps_160 = np.array(pickle.load(steps_160_file))

import pdb;pdb.set_trace()

times_diff = times_220 - times_260

steps_diff = steps_220 - steps_260

n_list = [n for n in range(1, 36)]

x = np.arange(0,36)
y = 2**x
fig_complexity_260 = plt.figure()
ax1 = fig_complexity_260.add_subplot(111)
ax1.plot(x, y, c = 'm', label = 'y = 2^x') 
ax1.scatter(n_list, steps_260, s=10, c='m', marker="*", label='Pasos')
plt.legend(loc='upper left')
plt.title('Complejidad')
plt.xlabel('N')
plt.ylabel('Pasos')
plt.show()

# # CPU 2.60 GHz 

# x = np.arange(0,36)
# fig_complexity_260 = plt.figure()
# ax1 = fig_complexity_260.add_subplot(111)
# ax1.plot(n_list, np.interp(n_list, n_list, times_260).tolist(), c = 'b', label = 'Interpolacion') 
# ax1.scatter(n_list, times_260, s=10, c='b', marker="s", label='2.60GHz')
# plt.legend(loc='upper left')
# plt.show()


# # CPU 2.20 GHz 

# x = np.arange(0,36)
# fig_complexity_220 = plt.figure()
# ax1 = fig_complexity_220.add_subplot(111)
# ax1.plot(n_list, np.interp(n_list, n_list, times_220).tolist(), c = 'r', label = 'Interpolacion') 
# ax1.scatter(n_list, times_220, s=10, c='r', marker="o", label='2.20GHz')
# plt.legend(loc='upper left')
# plt.show()

# # CPU 1.60 GHz 

# x = np.arange(0,36)
# fig_complexity_160 = plt.figure()
# ax1 = fig_complexity_160.add_subplot(111)
# ax1.plot(n_list, np.interp(n_list, n_list, times_160).tolist(), c = 'g', label = 'Interpolacion') 
# ax1.scatter(n_list, times_160, s=10, c='g', marker="v", label='1.60GHz')
# plt.legend(loc='upper left')
# plt.show()


fig_times_all = plt.figure()
ax1 = fig_times_all.add_subplot(111)

ax1.scatter(n_list, times_260, s=10, c='b', marker="s", label='2.60GHz')
ax1.scatter(n_list, times_220, s=10, c='r', marker="o", label='2.20GHz')
ax1.plot(n_list, np.interp(n_list, n_list, times_220).tolist(), c = 'r', label = 'Interpolacion')
ax1.plot(n_list, np.interp(n_list, n_list, times_260).tolist(), c = 'b', label = 'Interpolacion')  
plt.legend(loc='upper left')
plt.title('Tiempos de 2.60 y 2.20 GHz')
plt.xlabel('N')
plt.ylabel('Tiempo')
plt.show()


fig_times_all = plt.figure()
ax1 = fig_times_all.add_subplot(111)

ax1.scatter(n_list, times_260, s=10, c='b', marker="s", label='2.60GHz')
ax1.scatter(n_list, times_220, s=10, c='r', marker="o", label='2.20GHz')
ax1.scatter(n_list, times_160, s=10, c='g', marker="v", label='1.60GHz')
ax1.plot(n_list, np.interp(n_list, n_list, times_160).tolist(), c = 'g', label = 'Interpolacion')
ax1.plot(n_list, np.interp(n_list, n_list, times_220).tolist(), c = 'r', label = 'Interpolacion')
ax1.plot(n_list, np.interp(n_list, n_list, times_260).tolist(), c = 'b', label = 'Interpolacion')   
plt.legend(loc='upper left')
plt.title('Tiempos de 2.60, 2.20 y 1.60 GHz')
plt.xlabel('N')
plt.ylabel('Tiempo')
plt.show()
