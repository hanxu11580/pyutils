from abc import ABCMeta, abstractmethod

# metaclass=ABCMeta这个必须有，不然抽象就失效了
class Student_Abstract(object, metaclass=ABCMeta):
    def __init__(self, base_field):
        self._base_field = base_field
        
    @abstractmethod
    def do_abstract(self):
        pass
        
class Student(Student_Abstract):
    def __init__(self, name, age):
        # 给父类字段赋值
        super().__init__('hhh')
        self.name = name
        self.age = age
        
        self.__secret = "this is diary"
        
    def study(self):
        print(f'{self.name}, {self.age} is study')
        
    def watch_movie(self):
        if self.age >= 18:
            print(f'{self.name}, {self.age} watch 18+')
        else:
            print(f'{self.name}, {self.age} watch 18-')
            
    def __say_secret(self):
        print(f'say {self.__secret}')
        
    @staticmethod
    def check_1(self):
        print(f'check {self.name}')
    
    @staticmethod
    def check_2():
        print(f'check2...')
        
    # 克隆一个学生
    @classmethod
    def clone(cls):
        return cls('default_name', 0)
    
    # TypeError: Can't instantiate abstract class Student with abstract methods do_abstract
    def do_abstract(self):
        print(f'实现抽象方法, 不然会报上面的错')
        

if __name__ == '__main__':
    stu_xiaoming = Student("xiaoming", 19)
    stu_xiaoming.study()
    stu_xiaoming.watch_movie()
    
    stu_xiaohuang = Student("xiaoming", 10)
    stu_xiaohuang.study()
    stu_xiaohuang.watch_movie()
    
    # 报错 AttributeError: 'Student' object has no attribute '__secret'
    # print(stu_xiaohuang.__secret)
    # AttributeError: 'Student' object has no attribute '__say_secret'        
    # stu_xiaohuang.__say_secret()
    
    # 但是你还是可以使用特殊规则访问到
    print(stu_xiaohuang._Student__secret)
    stu_xiaohuang._Student__say_secret()
    
    # 静态方法
    Student.check_1(stu_xiaohuang)
    # 还能这样调用静态方法
    stu_xiaohuang.check_1(stu_xiaohuang)
    Student.check_2()
    
    
    # 克隆出一个学生
    stu_clone = Student.clone()
    print(f'clone student {stu_clone.name} {stu_clone.age}')
    
    # 把上面的super().__init__('hhh')删掉会报下面这个错
    # AttributeError: 'Student' object has no attribute '_base_field'
    print(stu_clone._base_field)