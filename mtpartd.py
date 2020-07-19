import threading
from time import ctime, sleep
loops=[4,2]
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
    def run(self):
        print("{} starts at {}".format(self.name,ctime()))
        self.ref=self.func(*self.args)
        print("{} end at {}".format(self.name,ctime()))
    def getRef(self):
        return self.ref

def loop(nloop,nsec):
    print("loop {} starts at {}".format(nloop,ctime()))
    sleep(nsec)
    print("loop {} ends at {}".format(nloop,ctime()))
def main():
    global loops
    threads=[]
    ranger=range(len(loops))
    for i in ranger:
        threads.append(MyThread(loop,(i,loops[i])))
    for i in ranger:
        threads[i].start()
    for i in ranger:
        threads[i].join()
    print("Main ends at ",ctime())
if __name__=="__main__":
    main()
