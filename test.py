#-*- codeing = utf-8 -*-
#@Time : 2020/12/7 下午 04:01
#@File : test.py
#@Softwore : PyCharm
import random
'''
a=int(input("请输入"))
print("%d"%a)
'''

'''
x=random.randint(0,10) #0-10之间随机取一个数字，包含0和10
print("%d\n"%x)

for i in range(0,10): #从0开始，9结束，步长默认为1
    print(i,end=' ')

print("\n")

for j in range(0,10,3): #从0开始，9结束，步长设置为3
    print(j,end=' ')

print("\n")

k=11;
for k1 in range(k):
    print(k1,end=' ')
'''
'''
l=['aa','bb','cc']
name='chengdu'
for n in name:
    print(n,end=' ')

print("\n")

for j in l:
    print(j,end=' ')

print("\n")

for i in range(len(l)):
    print(i,l[i],end=' ')
'''

count=0
while count<5:
    print("%d小于5"%count)
    count+=1
else:
    print("%d不小于5"%count)
'''在python里面while可以和else搭配使用'''
print("欢迎quietkk加入")
