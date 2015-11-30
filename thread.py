import threading, time

def loop_func():
    print('Thread %s is running' % threading.current_thread().name)
    for n in range(5):
        print('Thread %s >> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s is end' % threading.current_thread().name)


if __name__ == '__main__':
    print('Thread %s is running' % threading.current_thread().name)
    sub_thread = threading.Thread(target=loop_func, name='LoopThread')
    sub_thread.start()
    sub_thread.join()
    print('Thread %s is end' % threading.current_thread().name)
