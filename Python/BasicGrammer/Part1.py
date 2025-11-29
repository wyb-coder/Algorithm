# # TODO 这是一段注释
# import random
#
name = "Wang Yao Bin"
age = 21
num1 = num2 = 1
INF = 100
# 变量，Python类型可以理解为全是C++ Auto类型，弱类型
# help() 函数可以查看函数的帮助信息
# print(type(temp)) type() 函数可以查看变量的类型
#
# 基本输入输出
print(("%d %d %d")%(1, 2, 3)) #格式化输出

print(f"My name is {name}")
print("My name is {}".format(name))
# print("Hello", end="")  # end="" 不换行
# print(round(3.1415926, 2))  # round() 函数四舍五入
# input()  # 输入函数，默认输入类型str
# print(int(input()))
#
# # 运算符
# # ** 幂运算 // 整除运算
# print(3 ** 4)
# # and or not 逻辑运算符
#
# # if else elif
# if name == "帅":
#     print("True")
# elif 100 < age < 200 :
#     print("False")
# Max = num1 if num1 > num2 else num2
#
# # 循环
# i = random.randint(1, 10)
# while i < 10:
#     print(i)
#     i += 1
#     continue
# # range(begin, end, step) 生成一个序列 begin <= x < end
# for i in range(1, INF, 2):
#     break
#
# for j in name:
#     print(j, end="")
#     break
# else:
#     print("")  # for else 语句 循环正常执行完成，达到上限后输出内容
# print("\n")
# # 字符串
# firstName = name[0:4]  # 切片操作
# print(name.find("Wang"))
# name.replace("Wang", "Li")
# print(name.lower() + name.lower())
# print(type(name.split(" ")))
#
# # list
# list1 = name.split(" ")
# list1.append("Wang") # append() 函数在末尾添加元素
# list1.insert(1, "Yao") # insert() 函数在指定位置添加元素
# list1.pop() # pop() 函数删除末尾元素
# list1.pop(1) # 删除指定位置元素
# list1.remove("Yao") # 删除指定元素
# print(len(list1)) # len() 函数获取长度
# list1.reverse() # reverse() 函数翻转
# list1.sort() # sort() 函数排序
#
# tuple 元组
tuple1 = (1, 2, 3)
tuple1 = tuple1 + (4, 5, 6) # 元组不可变，但可以连接
tuple1 = tuple1 * 2 # 重复
# print(tuple1[1:3]) # 切片
# print(tuple1.count(1)) # count() 函数统计元素出现次数
# print(tuple1.index(3)) # index() 函数获取元素下标
# for i in tuple1:
#     print(i)
#
# dict 字典 哈希表，查找速度快
dict1 = {"name": "Wang", "age": 21}
print(dict1["name"]) # 获取元素
dict1["name"] = "Li" # 修改元素
dict1["帅"]  = "帅" # 添加元素
dict1.pop("name") # 删除元素
dict1.clear() # 清空字典
print(dict1.keys()) # 获取所有键
dict1.get("name") # 获取元素,不存在返回None
print(None == dict1.get("123e"))
for key, value in dict1.items():
    print(key, value)
#
# # set 集合 无序不重复元素序列
# set1 = {1, 2, 3}
# set1.add(4) # 添加元素
# set1.remove(1) # 删除元素
# set1.pop() # 随机删除元素
# set1.clear() # 清空集合
# set1 = set("123") # 通过字符串创建集合
# for i in set1:
#     print(i)
#
# # 推导式
# list2 = [x for x in range(1, 10) if x % 2 == 0]
#
# # 元组拆包
# a, b, c = (1, 2, 3)
# a, b, c = (c, a, b)
# print(a, b, c)
#
# # map() 函数 传入函数和序列，返回一个新的序列
# def f(x):
#     return x * x
# list3 = [1, 2, 3]
# list4 = list(map(f, list3))
# print(list4) # [1, 4, 9]
#
#
