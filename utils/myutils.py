from functools import wraps
from time import time
from time import sleep
from threading import RLock


#region 函数耗时装饰
def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__}: {end - start}秒')
        return result
    return wrapper

@record_time
def test_record_time():
    sleep(3)

#endregion
    
#region 线程安全单例装饰
def singleton(cls):
    instances = {}
    locker = RLock()
    
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)   
        return instances[cls]
    return wrapper

@singleton
class Test_singleton(object):
    def __init__(self, singleton_name):
        self.singleton_name = singleton_name
        
    def i(self):
        print(self.singleton_name)
    
    @staticmethod
    def test_singleton():
        test_instance_1 = Test_singleton("第一次创建的instance")
        test_instance_1.i()
        
        test_instance_2 = Test_singleton("第二次创建的instance")
        test_instance_2.i()
        
#endregion

#region 使用元类实现单例
class SingletonMeta(type):
    def __init__(cls, *args):
        cls.__instance = None
        cls.__lock = RLock()
        
    # 在Python中，__call__是一个特殊方法
    # 它使得一个对象可以像函数一样被调用
    # 换句话说，这个方法可以让我们定义当对象被当作函数调用时的行为
    # 类使用SingletonMeta作为它的元类，所以当你尝试实例化时，Python会调用SingletonMeta的__call__方法
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance
        
class Test_SingletonMeta(metaclass=SingletonMeta):
    def __init__(self, singleton_name):
        self.singleton_name = singleton_name
            
    def i(self):
        print(self.singleton_name)
                
    @staticmethod
    def test():
        test_instance_1 = Test_SingletonMeta("第一次创建的instance")
        test_instance_1.i()
        
        test_instance_2 = Test_SingletonMeta("第二次创建的instance")
        test_instance_2.i()
    
#endregion


if __name__ == '__main__':










    pass

    
        
            





