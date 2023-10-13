from time import time, sleep
from multiprocessing import Process

def download_something(file_name):
    if file_name == 'd1':
        down_time = 3
    elif file_name == 'd2':
        down_time = 5
    else:
        down_time = 10
        
    sleep(down_time)
    print(f'下载{file_name}，耗时:{down_time}')
    
def download_1():
    # 下载d1，耗时:3
    # 下载d2，耗时:5
    # 共耗时:8.01
    download_something('d1')
    download_something('d2')

def download_2():
    # 下载d1，耗时:3
    # 下载d2，耗时:5
    # 共耗时:5.08
    p1 = Process(target=download_something, args=('d1',))
    p1.start()
    p2 = Process(target=download_something, args=('d2',))
    p2.start()
    
    # 等待p1、p2结束
    p1.join()
    p2.join()
    
def print_time(func):
    start = time()
    func()
    end = time()
    print('共耗时:%.2f'%(end - start))
    
if __name__ == '__main__':
    print_time(download_1)
    print_time(download_2)
        
        
    