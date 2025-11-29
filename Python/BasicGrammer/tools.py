# 函数
def test(name):
    print("hello{}".format(name))
    return 1

def sum(N):
    if N == 1:
        return 1
    return N + sum(N - 1)

print(sum(100))

# 类
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "name:{} age:{}".format(self.name, self.age)
    def test(self):
        print("hello1")

Wyb = Student("Wang Yao Bin", 21)
# del Wyb

class Student2(Student):
    # 重写构造函数
    def __init__(self, name, age, score):
        super().__init__(name, age) # 调用父类构造函数
        self.score = score
    def __str__(self):
        return "name:{} age:{} score:{}".format(self.name, self.age, self.score)
    # pass 语句是空语句，是为了保持程序结构的完整性
    def test(self):
        print("hello2")

Czr = Student2("Czr", 21, 100)

# 多态
def printInfo(obj):
    obj.test()
printInfo(Wyb)

# 文件操作
fp = open("test.txt", "r") # w:写入，r:读取，a:追加
# 既可以读取又可以写入
fp1 = open("test.txt", "r+") # w+:写入和读取，r+:读取和写入，a+:追加和读取
# w+ 和 r+ 区别：w+会清空文件内容，r+不会
# fp.write("hello")
print(fp1.read()) # 读取文件
# with 语句 会自动关闭文件
with open("test.txt", "r") as fp2:
    print(fp2.read())

# 目录
import os
print(os.getcwd()) # 获取当前目录
print(os.listdir()) # 获取当前目录下的文件
print(os.path.exists("test.txt")) # 判断文件是否存在
print(os.path.isdir("test.txt")) # 判断是否是目录
print(os.path.isfile("test.txt")) # 判断是否是文件
print(os.path.join(os.getcwd(), "test.txt")) # 拼接路径
print(os.path.split(os.path.join(os.getcwd(), "test.txt"))) # 分割路径

# 异常处理
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e)
finally:
    print("finally")


