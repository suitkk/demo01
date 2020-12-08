#-*- codeing = utf-8 -*-
#@Time : 2020/12/8 下午 02:16
#@File : string.py
#@Softwore : PyCharm
'''
word='字符串1'#不能直接换行
sentence="字符串2"#不能直接换行
paragraph="""
        段落1
        段落2
        段落3
        
"""#可以直接换行
print(word)
print(sentence)
print(paragraph)
'''
'''
str="chengdu"
print(str)
print(str[2])
print(str[5])
print(str[-5])
print(str[-5:-2])
print(str[2:5])
print(str[:5])
print(str[1:6:2])#[开始位置：结束位置（不包括）：步长]
'''
'''
print("hello\nchengdu")#\为转义
print(r"hello\nchengdu")#最前面的r为取消转义
str='fg'
print(str.isalnum())#如果字符串由字母或数字组成，则为true
print(str.isalpha())#如果字符串由字母组成，则为true
print("1234".isdigit())#如果字符串由数字(0-9和罗马数字)组成，则为true
print("1234".isdecimal())#如果字符串由数字(0-9)组成，则为true
print("Ⅷ".isdigit())
print("Ⅷ".isnumeric())#如果字符串由数字(0-9、罗马数字、汉字)组成，则为true
'''

list1=[1,'1',(1),(1,'1')]
print(type(list1[0]))
print(type(list1[1]))
print(type(list1[2]))
print(type(list1[3]))
print(type(list1[3][0]))
print(type(list1[3][1]))
list2=(1)#只有一个元素的元组不是元组
list3=[1]#只有一个元素的列表仍是列表
list4=(1,)#只有一个元素的元组表示方式
print(type(list2))
print(type(list3))
print(type(list4))
print(len(list4))