from __future__ import division
import numpy as np
import matplotlib.pyplot as plt 
import math
from prettytable import PrettyTable
    
pt = PrettyTable()


x = np.arange(1,11)

y1 = x.cumprod()
y2 = np.exp(x)
y3 = 2**x
y4 = x**3
y5 = x*np.log(x)
y6 = np.log(x)

fig_functions = plt.figure()
ax1 = fig_functions.add_subplot(111)
ax1.plot(x, y6, c = 'k', label = 'ln(n)') 
plt.legend(loc='upper left')
plt.title('Comparacion de Funciones')
plt.xlabel('N')
plt.ylabel('Y')
plt.show()

fig_functions = plt.figure()
ax1 = fig_functions.add_subplot(111)
ax1.plot(x, y5, c = 'm', label = 'n*ln(n)') 
ax1.plot(x, y6, c = 'k', label = 'ln(n)') 
plt.legend(loc='upper left')
plt.title('Comparacion de Funciones')
plt.xlabel('N')
plt.ylabel('Y')
plt.show()

fig_functions = plt.figure()
ax1 = fig_functions.add_subplot(111) 
ax1.plot(x, y4, c = 'c', label = 'n^3') 
ax1.plot(x, y5, c = 'm', label = 'n*ln(n)') 
ax1.plot(x, y6, c = 'k', label = 'ln(n)') 
plt.legend(loc='upper left')
plt.title('Comparacion de Funciones')
plt.xlabel('N')
plt.ylabel('Y')
plt.show()

fig_functions = plt.figure()
ax1 = fig_functions.add_subplot(111)
ax1.plot(x, y3, c = 'r', label = '2^n') 
ax1.plot(x, y4, c = 'c', label = 'n^3') 
ax1.plot(x, y5, c = 'm', label = 'n*ln(n)') 
ax1.plot(x, y6, c = 'k', label = 'ln(n)') 
plt.legend(loc='upper left')
plt.title('Comparacion de Funciones')
plt.xlabel('N')
plt.ylabel('Y')
plt.show()

fig_functions = plt.figure()
ax1 = fig_functions.add_subplot(111)
ax1.plot(x, y2, c = 'g', label = 'e^n') 
ax1.plot(x, y3, c = 'r', label = '2^n') 
ax1.plot(x, y4, c = 'c', label = 'n^3') 
ax1.plot(x, y5, c = 'm', label = 'n*ln(n)') 
ax1.plot(x, y6, c = 'k', label = 'ln(n)') 
plt.legend(loc='upper left')
plt.title('Comparacion de Funciones')
plt.xlabel('N')
plt.ylabel('Y')
plt.show()

fig_functions = plt.figure()
ax1 = fig_functions.add_subplot(111)
ax1.plot(x, y1, c = 'b', label = 'n!')
ax1.plot(x, y2, c = 'g', label = 'e^n') 
ax1.plot(x, y3, c = 'r', label = '2^n') 
ax1.plot(x, y4, c = 'c', label = 'n^3') 
ax1.plot(x, y5, c = 'm', label = 'n*ln(n)') 
ax1.plot(x, y6, c = 'k', label = 'ln(n)') 
plt.legend(loc='upper left')
plt.title('Comparacion de Funciones')
plt.xlabel('N')
plt.ylabel('Y')
plt.show()

# Table: 

pt.field_names = x
pt.add_row(y1)
pt.add_row(y2)
pt.add_row(y3)
pt.add_row(y4)
pt.add_row(y5)
pt.add_row(y6)

print(pt)

# Primes! 

x = np.arange(1,5001)
y5 = x*np.log(x)

count = 0

def prime(n):
    global count

    if n <= 1:
        return False
    count += 1
    if n == 2:
        return True 
    count += 1  
    if n % 2 == 0:
        return False
    count += 1
    d = 3
    while d * d <= n:
        if (n % d == 0):
            return False
        count += 1
        d += 2 
    return True

def count_primes_division(n):
    global count
    primes = 0
    i = 1
    while(i <= n):
        count += 1
        if prime(i):
            primes += 1
        i += 1
    return primes


steps_primes_division = []

for n in x:
	count = 0
	count_primes_division(n)
	steps_primes_division.append(count)

fig_functions = plt.figure()
ax1 = fig_functions.add_subplot(111)
ax1.plot(x, y5, c = 'm', label = 'n*ln(n)') 
ax1.plot(x, steps_primes_division, c = 'y', label = 'Primes with Division') 
plt.legend(loc='upper left')
plt.title('Comparacion de Funciones')
plt.xlabel('N')
plt.ylabel('Y')
plt.show()

def primes_division_complexity(n):
	sum = 0
	for i in range(1,n+1):
		sum = sum + math.sqrt(i) / 2
	return sum

y7 = [primes_division_complexity(n) for n in x]

fig_functions = plt.figure()
ax1 = fig_functions.add_subplot(111)
ax1.plot(x, y5, c = 'm', label = 'n*ln(n)') 
ax1.plot(x, steps_primes_division, c = 'y', label = 'Primes with Division')
ax1.plot(x, y7, c = 'r', label = 'Primes with Division Bound') 
plt.legend(loc='upper left')
plt.title('Comparacion de Funciones')
plt.xlabel('N')
plt.ylabel('Y')
plt.show()