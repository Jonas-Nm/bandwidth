import matplotlib.pyplot as plt
import numpy as np

file = 'vna_remote.txt'

with open(file, "r") as lines:
    lines = lines.readlines()[1:]
    freq = [float(x.split(' ')[0]) for x in lines]
    s21 = [float(x.split(' ')[2]) for x in lines]

print(freq[1])
print(s21[1])
print(len(freq))
print(len(s21))

plt.figure()
plt.plot(freq,s21)
plt.show()

