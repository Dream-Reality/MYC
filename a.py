import random
import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt
d = 18

a = [[] for i in range(d)]
l = []
cnt = 0
total = 10000000
for i in range(total):
    res = 0
    tmp = []
    for j in range(d):
        tmp.append(random.random()*2-1)
    for j in range(d):
        res += tmp[j]*tmp[j]
    if res<1.:
        for j in range(d):
            a[j].append(tmp[j])
        cnt += 1
        l.append(res)
print(l)
s = sum(l)/len(l)
p = len(l)/total
print(s,p*(2**d))

