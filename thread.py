import threading, time

def loop_func():
    print('Thread %s is running' % threading.current_thread().name)
    for n in range(5):

