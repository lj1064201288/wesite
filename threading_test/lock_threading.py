import time, threading


def fun_1():
    print('函数1开始执行...')
    time.sleep(1)

    lock_1.acquire()
    print('函数1上第一把锁....')
    time.sleep(2)

    lock_2.acquire()
    print('函数1上第二把锁....')
    time.sleep(3)

    lock_1.release()
    print('函数1第二把锁解锁...')
    time.sleep(2)

    lock_2.acquire()
    print('函数1第二把锁锁上...')



def fun_2():
    print('函数2开始执行...')
    time.sleep(2)

    lock_1.release()
    print('函数2解开第一把锁...')
    time.sleep(2)

    lock_2.release()
    print('函数2解开第二把锁上锁...')
    time.sleep(1)

    lock_1.acquire()
    print('函数2申请解锁第一把锁....')
    time.sleep(4)

    lock_2.release()
    print('函数2申请解锁第二把锁...')





if __name__ == '__main__':

    lock_1 = threading.Lock()
    lock_2 = threading.Lock()


    t1 = threading.Thread(target=fun_1, args=())
    t2 = threading.Thread(target=fun_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

