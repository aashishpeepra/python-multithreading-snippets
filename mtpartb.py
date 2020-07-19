import _thread
from time import ctime,sleep
loops=[4,2]
def loop(nloop,nsec,lock):
    print("loop {} starts at {}".format(nloop,ctime()))
    sleep(nsec)
    print("loop {} ends at {}".format(nloop,ctime()))
    lock.release()
def main():
    global loops
    print("Main starts at ",ctime())
    locks=[]
    for i in range(len(loops)):
        lock=_thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in range(len(loops)):
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in range(len(loops)):
        while locks[i].locked():
            pass
    print("Main ends at ",ctime())
if __name__=="__main__":
    main()