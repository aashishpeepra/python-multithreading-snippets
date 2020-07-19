from time import ctime, sleep
from threading import Thread
loops=[4,2]
def loop(nloop,nsec):
    print("loop {} starts at {}".format(nloop,ctime()))
    sleep(nsec)
    print("loop {} ends at {}".format(nloop,ctime()))
def main():
    global loops
    print("Main starts at ",ctime())
    threads=[]
    ranger=range(len(loops))
    for i in ranger:
        threads.append(Thread(target=loop,args=(i,loops[i])))
    for i in ranger:
        threads[i].start()
    for i in ranger:
        threads[i].join()
    print("Main ends at ",ctime())
if __name__=="__main__":
    main()