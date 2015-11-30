import threading

# global vir
balance = 0
lock = threading.Lock()


def change(n):
    global balance
    balance += n
    balance -= n


def thread_fun(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


t1 = threading.Thread(target=thread_fun, args=(5,))
t2 = threading.Thread(target=thread_fun, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
