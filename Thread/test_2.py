from time import time, sleep
from threading import Thread
    
def print_time(func):
    start = time()
    func()
    end = time()
    print('共耗时:%.2f'%(end - start))


class DownloadThread(Thread):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        
    # 重写了Threa的Run方法，换个名字就不行了
    def run(self):
        self.__download_something()
        
    def __download_something(self):
        if self.__file_name == 'd1':
            down_time = 3
        elif self.__file_name == 'd2':
            down_time = 5
        else:
            down_time = 10
        sleep(down_time)
        print(f'下载{self.__file_name}，耗时:{down_time}')
    
def execute():
    t1 = DownloadThread('d1')
    t1.start()
    
    t2 = DownloadThread('d2')
    t2.start()
    
    t1.join()
    t2.join()            

    
if __name__ == '__main__':
    print_time(execute)
    
    
    
    