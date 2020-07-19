from time import ctime, sleep

def loop0():
    print("loop 0 starts at ",ctime())
    sleep(4)
    print("loop 0 ends at ",ctime())
def loop1():
    print("loop 1 starts at ",ctime())
    sleep(2)
    print("loop 1 ends at ",ctime())
def main():
    print("Main starts at ",ctime())
    loop0()
    loop1()
    print("Main ends at ",ctime())
if __name__=="__main__":
    main()