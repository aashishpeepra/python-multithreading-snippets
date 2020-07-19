from mtpartd import MyThread
from time import ctime,sleep

def fib(n):
    sleep(0.005)
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
def fac(x):
    sleep(.1)
    if x<=1:
        return 1
    else:
        return x*fac(x-1)
def sum(x):
    sleep(.1)
    if x<=1:
        return 1
    else:
        return x+sum(x-1)
funcs=[fac,sum]
number=12
def main():
    ranger=range(len(funcs))
    print("***Non Threaded***")
    for i in ranger:
        print("{} starts at {}".format(funcs[i].__name__,ctime()))
        print(funcs[i](number))
        print("{} ends at {}".format(funcs[i].__name__,ctime()))
    threads=[]
    print("***Threaded***")
    for i in ranger:
        threads.append(MyThread(funcs[i],(number,),funcs[i].__name__))
    for i in ranger:
        threads[i].start()
    for i in ranger:
        threads[i].join()
        print(threads[i].getRef())
    print("All done!")
if __name__=="__main__":
    main()