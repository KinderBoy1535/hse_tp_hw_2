from time import time
from tz2 import _max, _min, _sum, _mult
from random import randint
import matplotlib.pyplot as plt

chisla = []
kolvo = []
vremya = []
for i in range(1, 1_000_002, 100000):
    if i == 1_000_001:
        i = 1_000_000
    chisla = [randint(-1000, 1000) for q in range(i)]
    starttime = time()
    _max(chisla)
    _sum(chisla)
    _min(chisla)
    _mult(chisla)
    finishtime = time()
    kolvo.append(i)
    vremya.append(finishtime - starttime)

plt.title('tz2')
plt.xlabel('Количество чисел (млн)')
plt.ylabel('Время выполнения (сек)')
plt.plot(kolvo, vremya)
plt.show()
