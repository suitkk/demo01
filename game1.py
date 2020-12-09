#-*- codeing = utf-8 -*-
#@Time : 2020/12/4 下午 04:36
#@File : game1.py
#@Softwore : PyCharm

def charge(a,b):
    if(a=='石头'):
        if(b=='石头'):
            req='平局'
        if (b == '剪刀'):
            req = '你输了'
        if (b == '布'):
            req = '你赢了'
    if (a == '剪刀'):
        if (b == '石头'):
            req = '你赢了'
        if (b == '剪刀'):
            req = '平局'
        if (b == '布'):
            req = '你输了'
    if (a == '布'):
        if (b == '石头'):
            req = '你输了'
        if (b == '剪刀'):
            req = '你赢了'
        if (b == '布'):
            req = '平局'
    return req