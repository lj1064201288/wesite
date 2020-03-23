import time
import threading
import queue

q = queue.Queue()


class Produce(threading.Thread):
    def run(self):
        global q

        count = 0

        while True:
            if q.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = '成品' + str(count)
                    q.put(msg)

                    print(msg)

            time.sleep(3)


class Consumer(threading.Thread):
    def run(self):
        global q

        while True:
            if q.qsize() > 100:
                for i in range(10):
                    msg = self.name + '消费了' + q.get()
                    print(msg)

            time.sleep(2)


if __name__ == '__main__':

    print('Start Production....')

    # for i in range(500):
    #     q.put('初始产品:' + str(i))

    for i in range(5):
        p = Produce()
        p.start()

    for i in range(3):
        c = Consumer()
        c.start()

