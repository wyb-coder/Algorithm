


Arr = [1, 3, 2, 6, 5, 2]
S = "This is a string for test"

# 1.同时枚举数组(列表)的位序与值
for index, value in enumerate(Arr):
    print(index, value)

# 2.字符串拼接 + 排除子串
s = ''.join(cr for cr in S if cr not in "aeiou")
print(s)