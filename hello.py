#-*- codeing = utf-8 -*-
#@Time : 2020/12/4 上午 11:39
#@File : hello.py
#@Softwore : PyCharm
import  random
import game1
#这是单行注释
print("hello")
'''
这是多行注释的第一行
这是多行注释的第二行
'''

'''
age=18
print("小张的年龄是：%0*.*f"%(10,2,age))
'''
'''
password=int(input("请输入第一条："))
typ=type(password)
print("输入类型为：%s\n输入的内容是：%s\n"%(type(password),password))

password2=input("请输入第二条：")
typ=type(password2)
print("输入类型为：%s\n输入的内容是：%s"%(type(password2),password2))
'''

'''
a={"1":"11","2":"2","3":"3"}
b='dfvf'
c=(1,2,3)
d=[1,2,3]
print(type(d))
'''


#l=['1','2','3','4','5']
#answer=input("现在开始猜数字游戏，请输入一个1-5的数字：")
#right=random.choice(l)
#while(answer!=right):
#    answer=input("错了！再来：")
#print("正确答案'''是%s\t恭喜你答对了！"%right)

print("现在开始石头剪刀布游戏\n")
l2=['石头','剪刀','布']
l3='1230'
con=1
while(con):
    an = int(input("请输入你的选择（1.石头，2.剪刀，3.布，0.不来了）："))
    if(an==0):
        break
    con=an
    if(l3.find(str(con))==-1):
        print("请输入正确的选项")
        continue
    else:
        answer = l2[an - 1]
        right = random.choice(l2)
        res = game1.charge(right, answer)
        print("我出的是：%s\n你出的是：%s\n%s" % (right, answer, res))
print("下次再来刚刚！")
