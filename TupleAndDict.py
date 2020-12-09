#-*- codeing = utf-8 -*-
#@Time : 2020/12/9 下午 03:55
#@File : TupleAndDict.py
#@Softwore : PyCharm

#元组不可更改

info={"name":"jack","age":19,"address":"Landon.England"}
print(info["name"])
print(info["age"])
print(info["address"])
#若直接访问不存在的键会报错
'''
print(info["gender"])
Traceback (most recent call last):
  File "E:/suit/demo/demo01/TupleAndDict.py", line 13, in <module>
    print(info["gender"])
KeyError: 'gender'
'''
print(info.get("gender"))#get不存在的键会得到none，但不会报错
print(info.get("gender","男"))#get不存在的键且设置默认值
print(info)

#dict增
info["id"]=1001
print(info)

#dict删
#1.del
info1={"name":"jack","age":19,"address":"Landon.England"}
print(info1)
del info1["address"]
print(info1)
#2.clear
info2={"name":"jack","age":19,"address":"Landon.England"}
print(info2)
info2.clear()
print(info2)

#dict改
info3={"name":"jack","age":19,"address":"Landon.England"}
print(info3)
info3["age"]=20
print(info3)

#dict查
info4={"name":"jack","age":19,"address":"Landon.England"}
print(info4.keys())
print(info4.values())
print(info4.items())

for key,value in info4.items():
    print("key:%s\t\tvalue:%s"%(key,value))
