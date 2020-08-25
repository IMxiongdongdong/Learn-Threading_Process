import threading
from queue import Queue
import time

time.start()


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)


def multithreading():
    q = Queue()
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    threads=[]
    for i in range(3):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    results = []
    for _ in range(3):
        results.append(q.get())
    print(results)


if __name__ == '__main__':
    multithreading()
