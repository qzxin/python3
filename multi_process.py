from multiprocessing import Process
import os


def run_proc(name):
    print('Run chiled process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent Process %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child Process will start:')
    p.start()
    p.join()
    print('Child Procee end')
