import time
import threading
import queue

sum = 0
LoopSum = 1000000
loop = [4, 2]

lock = threading.Lock()

def add_sum():

    global sum, LoopSum

    for i in (1, LoopSum):
        lock.acquire()
        sum += 1
        lock.release()

def minus_sum():

    global sum, LoopSum

    for i in range(1, LoopSum):
        lock.acquire()
        sum -= 1
        lock.release()



if __name__ == '__main__':

    print('Start.....Threadtest....{}'.format(time.ctime()))

    t1 = threading.Thread(target=add_sum, args=())
    t2 = threading.Thread(target=minus_sum, args=())

    t1.start()
    t2.start()

    print('End....time....{}'.format(time.ctime()))
    print(sum)