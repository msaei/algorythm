def bubbleSort(alist):
    n = 0
    swaped = True
    for passnum in range(len(alist)-1,0,-1):
        n += 1
        if not swaped:
            break
        swaped = False
        for i in range(passnum):
            
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                swaped = True
    return n

def log_n(lists):
    return [bubbleSort(l) for l in lists]

import random
def generate_list(listNum, listRange):
    result = []
    for i in range(listNum):
        alist = [ i for i in range(listRange)]
        random.shuffle(alist)
        result.append(alist)
    return result

lists = generate_list(1000,10)
ns = log_n(lists)
#print(ns)
x = list(set(ns))
y = [ ns.count(i) for i in x]
xy = 0
for i in range (len(x)):
    xy += x[i] * y[i]
print(xy/1000)

import matplotlib.pyplot as plt

plt.bar(x,y,label='bar')
plt.xlabel('passes')
plt.ylabel('quantity')
plt.title('bubble sort performance over a 1000 random list')
plt.show()