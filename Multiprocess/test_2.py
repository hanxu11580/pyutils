from time import time, sleep
from multiprocessing import Process
from multiprocessing import Queue


# 定义一个特殊的哨兵值
sentinel = -1

def do_something(q:Queue, some_str):
    while True:
        counter = q.get()
        
        if counter == sentinel:
            break
           
        if counter < 10:
            print(some_str)
            counter += 1
            q.put(counter)
        else:
            q.put(sentinel)
            break
        
# 打印a、b共10次        
if __name__ == '__main__':
    q = Queue()
    q.put(0)
    
    p1 = Process(target=do_something, args=(q, 'a',))
    p1.start()
    p2 = Process(target=do_something, args=(q, 'b',))
    p2.start()
    
    # 等待p1、p2结束
    p1.join()
    p2.join()