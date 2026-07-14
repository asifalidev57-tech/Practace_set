import threading
import time

def number():
    for i in range(5):
        time.sleep(2)
        print(f"The number is {i} ")


def alphabet():
    for letter in 'abcde':
        time.sleep(2)
        print(f"The letter are:{letter}")


#creating multithreading
t1=threading.Thread(target=number)
t2=threading.Thread(target=alphabet)

t=time.time()
t1.start()
t2.start()


t1.join()
t2.join()

finished=time.time()-t
print(finished)