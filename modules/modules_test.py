
import modules_1
import modules_2


# 大家都定义foo
# 如果一个文件都定义foo会出问题
if __name__ == '__main__':
    modules_1.foo()
    modules_2.foo()
    