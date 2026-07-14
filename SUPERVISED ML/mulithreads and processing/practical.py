
import multiprocessing
import time


def number(n):
    for i in range(n):
     time.sleep(2)
     print(i)

p1=multiprocessing.process(target=number(5))

p1.start()
p1.join()