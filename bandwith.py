import matplotlib.pyplot as plt
import numpy as np

file = 'vna_remote.txt'

with open(file, "r") as lines:
    lines = lines.readlines()[1:]
    freq = [float(x.split(' ')[0]) for x in lines]
    s21 = [float(x.split(' ')[2]) for x in lines]

s21_max = np.max(s21)
index = s21.index(s21_max)
s21_3dB = np.max(s21)-3.0
def find_nearest(array, value):
    array_left = np.asarray(array[:index])
    array_right = np.asarray(array[index:-1])
    idx_left = (np.abs(array_left - value)).argmin()
    idx_right = (np.abs(array_right - value)).argmin()
    return array[idx_left], idx_left, array[idx_right+index], idx_right+index
f = find_nearest(s21, s21_3dB)

f_0 = freq[index]  #fallunterscheidung, wann wie runden und welche Einheit! zB. unter 10MHz 2 Stellen bei f0, wann bw in kHz oder MHz?
bw = np.abs(freq[f[1]]-freq[f[3]])
f0_MHz = np.round(f_0/1E6, 2) #MHz
bw_kHz = np.round(bw/1E3, 1) #kHz
Q = int(np.round(f_0/bw,0))

print(Q)