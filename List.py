#-*- codeing = utf-8 -*-
#@Time : 2020/12/8 下午 03:47
#@File : List.py
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


#删1.del删除指定下标对应元素
movie=["变形金刚1","加勒比海盗","阿凡达","太空救援","盗梦空间"]
print("------删除前------")
for name in movie:
    print(name)
del movie[2]
print("------删除后------")
for name in movie:
    print(name)

#删2.pop 删除最后一个元素
movie2=["战狼","红海行动","建军大业","太空救援","盗梦空间"]
print("------删除前------")
for name in movie2:
    print(name)
movie2.pop()
print("------删除后------")
for name in movie2:
    print(name)

#删3.remove 删除指定元素
movie3=["战狼","红海行动","建军大业","太空救援","盗梦空间"]
print("------删除前------")
for name in movie3:
    print(name)
movie3.remove("太空救援")#删除匹配到的第一个
print("------删除后------")
for name in movie3:
    print(name)

l2=['q','b','d','s','a','f']
print(l2.index('a',1,5))#index(值，开始位置，结束位置)，开始和结束位置可不填

l3=[1,3,2,4]
l3.sort()
print(l3)
l3.reverse()
print(l3)


product=[["iphone11pro",6999],["xiaomi10",4999],["honer30",3699],["huaweiP40",4599],["meizu17",2199],["oppo r17",1999]]
choice=''
index=0
print("%-2s\t%-15s\t%-15s"%("编号","商品名称","商品价格"))
for name in product:
    print("%-4d\t%-15s\t%-15d"%(index,product[index][0],product[index][1]))
    index+=1
shoplist=[]
sum=0
while choice!='q':
    choice=input("您想要买什么？(按q结算):")
    if(choice=='q'):
        break
    c=int(choice)
    shoplist.append(product[c])
    sum+=product[c][1]
print("%-15s\t%-15s"%("商品名称","商品价格"))
sumlist=["共计消费",sum]
shoplist.append(sumlist)
for good in shoplist:
    print("%-15s\t￥%-15d"%(good[0],good[1]))


