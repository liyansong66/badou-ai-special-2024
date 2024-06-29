import numpy
import matplotlib.pyplot as plt
import numpy as np


def Normalization1(x):
    return [(float(i)-min(x))/float(max(x)-min(x)) for i in x]

def Normalization2(x):
    return [(float(i)-np.mean(x))/float(max(x)-min(x)) for i in x]


def z_score(x):
    r = sum([(i-np.mean(x))*(i-np.mean(x)) for i in x])/len(x)
    return [(i-np.mean(x))/r for i in x]

l=[-10, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 30]
l1=[]
cs=[]
for i in l:
    c=l.count(i)
    cs.append(c)
print(cs)

n=Normalization1(l)
z=z_score(l)
print(n)
print(z)
plt.plot(l,cs)
plt.plot(z,cs)
plt.show()