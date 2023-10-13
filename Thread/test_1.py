from time import time, sleep
from threading import Thread

def download_something(file_name):
    if file_name == 'd1':
        down_time = 3
    elif file_name == 'd2':
        down_time = 5
    else:
        down_time = 10
        
    sleep(down_time)
    print(f'下载{file_name}，耗时:{down_time}')
    
def print_time(func):
    start = time()
    func()
    end = time()
    print('共耗时:%.2f'%(end - start))

def download_thread():
    # 下载d1，耗时:3
    # 下载d2，耗时:5
    # 共耗时:5.08
    t1 = Thread(target=download_something, args=('d1',))
    t1.start()
    
    t2 = Thread(target=download_something, args=('d2',))
    t2.start()
    
    t1.join()
    t2.join()
    
if __name__ == '__main__':
    print_time(download_thread)
    
    