#-*- codeing = utf-8 -*-
#@Time : 2020/12/8 下午 03:47
#@File : list.py
#@Softwore : PyCharm


namelist=["小王","小张","小李"]
#list的增删改查
#增1.append
print("--------增加前-------")
for name in namelist:
    print(name)

print("--------增加后-------")
namelist.append("小刘")
for name in namelist:
    print(name)


#增2.extend
a=[1,2]
a1=[1,2]
b=[3,4]
a.append(b)
a1.extend(b)
print(a)
print(a1)


#增3.insert
l1=[0,1,2]
l1.insert(1,9)#insert(位置，值)
print(l1)
l1.insert(1,'s')
print(l1)
print(l1.index(9))


#删1.del
movie=["变形金刚1","加勒比海盗","阿凡达","太空救援","盗梦空间"]
print("------删除前------")
for name in movie:
    print(name)
del movie[2]
print("------删除后------")
for name in movie:
    print(name)