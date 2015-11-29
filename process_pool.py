from multiprocessing import Pool
import time, os, random



def long_time_task(name):
    print('running process %s(%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('sleep time is %0.2f' % (end-start))

if __name__ == '__main__':
    p = Pool(5)
    for i in range(10):
        p.apply_async(long_time_task, args = (i,))
    print('waiting subprocess done...')
    p.close()
    p.join()
    print('All subprocess done')
