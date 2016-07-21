# ASCII Art for text
# https://www.hackerearth.com/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
from PIL import Image


# else if  elif!
print('===============if else elif===============')
if bool(3>4):
    print(123)
elif bool (4==3):
    print(312)
else:
    print('elif' , 111, '\n')

# list
print('===============list===============')
a= []
print(type(a))  # Class
print(bool(a))  # bool 有没有值
print(a)

b= [1,'hello','2',1]
print(b)
print(b[1])  # 索引
print(b[:2])  # 不包含结束位置
print(b[-1])  # 负数从右开始
print('b的长度',len(b),'\nb的类型',type(b))

x=['meme','haha',1]    # 合并2个list
b.extend(x)
print('拼接后的b',b, "extend的对象是list\n")

# 出现次数
la = [1 ,2 ,3 , 1, 1,3,'haha']
print('1的出现次数',la.count(1))
print('haha的位置',la.index('haha'))

la.insert(3,'meme')
print('在第三位 insert meme',la)

# la.remove('meme') # 删除
# print('删除后',la)

if 'm1eme' in la:
    la.remove('meme')
else:
    print('m1eme不在la里面')

print('pop3 前的la',la)
la.pop(3)   # pop是移除index的元素
# la.remove(3) # remove是移除元素
print('pop3 后的la',la)

# rg = range(0, 100,2)
# print(rg)

nb = [1,4,5,6,7,9,0,12]
nb.sort()
nb.sort(reverse=True) # 实现倒叙

print('sort 排序',nb)

# print(help(list))

str = 'haha,nihao\mnade;shabi'
print(str.split(';')) #分割字符串

name = ['Roland','Lee','haha']
print('...'.join(name),'\n')


# for
print('===============for 语句===============')

aligut = []
for i in range(1,100):
    if i % 3 == 0:
        aligut.append(i)
print('写法1',aligut)

bligut = [i for i in list(range(1,100)) if i%3==0]
print('写法2',bligut)

cligut = list(range(3,100,3))  # python3 range外面要加个list!!!
print('写法3',cligut)

# s = "  \t a string example\t  "
# s = s.strip()
# print('s is',s)  # 去除空格

print('range 外面要加list',list(range(0,100,15)))


