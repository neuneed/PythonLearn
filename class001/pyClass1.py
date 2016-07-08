#coding:utf-8

def spam():
    eggs=12
    return eggs

print(spam())



hello = a = ['spam', 'eggs', 100, 1234,[2, 3, 'xtra']]

print(hello)

c = len(a)

print(c ,'and',len(a))

print("the max num is",max(123,1111))

print("hello is",a)

print(round(123.45512312,2))     # 四舍五入
print(abs(-1.23))                # 求绝对值
print(pow(2,13))                 # 幂函数 2的3次方

import math
print(math.floor(32.6))         # 取整 不是四舍五入
print(math.sqrt(4))             # 开平方

print(type(math.sqrt(9)))       # 类型判断

print(2/5)
print(5%2)                      # 余数
print(divmod(5,2))              # 返回(2,1) 商和余数
print(round(1.2332,2))


# 函数的构建
def add_function (a ,b ):
    c = a+b
    print(c)

# 函数的使用
add_function(123,1)


if __name__ == "__main__":
    add_function(1,23)


def fuckObjectiveC (fuckC, fuckq):
    if fuckC <100:
        fuckq = fuckC
    print("fuckOC result",fuckq)

fuckObjectiveC(12,1123)

print("what the fuck \"oc\"")


def myadd(a = 1,b =100):
    result = 0
    i = a
    while i <= b:
        result += i
        i += 1
    return result
print('my add is ', myadd())

