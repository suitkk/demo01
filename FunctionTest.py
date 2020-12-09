#-*- codeing = utf-8 -*-
#@Time : 2020/12/9 下午 04:55
#@File : FunctionTest.py
#@Softwore : PyCharm

#多个返回值的函数
# def divid(a,b):
#     shang=a//b
#     yushu=a%b
#     return shang,yushu
# n1=int(input("请输入被除数："))
# n2=int(input("请输入除数："))
# x,y=divid(n1,n2)
# print("%d÷%d=%d...%d"%(n1,n2,x,y))

def fun1():
    print("--------------")
def fun2(n):
    for i in range(n):
        fun1()
def fun3(a,b,c):
    return a+b+c
def fun4(a,b,c):
    ava=fun3(a,b,c)/3
    return ava
fun2(5)
print(fun4(2,5,92))