# 包含学生类
# 一个sayhello函数
# 一个打印语句

class Student():
    def __init__(self, name = 'NoName', age = 19):
        self.name = name
        self.age = age

    def say(self):
        print('My name is {0}'.format(self.name))

def sayHello():
    print('Hi, welcome to tuling')

# 下面的判断句意思是，只有当执行的是当前的文件，才执行之后的语句
# 建议作为程序的入口
if __name__ == '__main__':
    print('It is packet_01')
