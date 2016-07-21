# coding:utf-8

hello = 'world'

for i in range(len(hello)):
    print(hello[i])
#  range(len(hello)) == range(5) == [0,1,2,3,4]

# python list解析  x**2是平方
squares = [x**2 for x in  range(1,10)]
print(squares)

listcansquet3 = [i for i in  range(1,100) if i%3 ==0]
print(listcansquet3)


# enumerate 遍历函数
weak = ['monday','sunday','friday']
for (i ,day) in enumerate(weak):
    print(day +' is ' + str(i) )


def treatment(pos,element):
    print( '%d :%s' %(pos,element))

[treatment(i,ele) for i ,ele in enumerate(weak)]


# ==================== Dic =========================
person = {'name':'neuneed','site':'www.google.com','language':'python'}
print(person['name'])
person['name2']='xcodell'  #添加key value ////插入到最前面
print(person['name2'])


# dic新建
website = {}.fromkeys(("third","force"),"facebook")
print(website)

for key in person:
    print(key)

website = {1: 'google', '2':'nuenedd' , '3':'yahoo' ,4: "apple"}
print(website)
new_web = website.copy()    # 浅拷贝

new_web.pop('2')   # 删除键值
print('删除后的原来的',website)
print('删除后的新的  ',new_web)

cnweb = {5: 'baidu', '6':'sina' , '7':'tencent' ,8: "taobao"}

website.update(cnweb)
print(website)



# ==================== 元祖 tuple =========================
print('\n\n ==================== 元祖 tuple=========================')
name = (['frist','google'],['second','yahoo'])
print(name)

t = 123, 'abc' ,['come' ,'here']
print(type(t))
print(t)

# ==================== set=========================
print('\n\n ==================== set =========================')
s1 = set('neuneedhelpme')
print(s1)

s2 = set([123,"google","face","book","facebook","book"])
print(s2)

# set can  'add', 'clear', 'copy', 'difference',
# 'difference_update', 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

s3 = frozenset('qiwsir')
print(s3)


str123 = '哈哈傻比'
print(str123) #python3 解决了 coding的问题

