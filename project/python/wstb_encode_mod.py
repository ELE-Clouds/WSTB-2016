#!/usr/bin/env python
#-*- coding:utf-8 -*-
#by Python2.7
import urllib

enType={'utf8':'UTF-8','gbk':'GBK','gb2312':'GB2312'}

#utf-8编码
def keyEncode(_strKey,_enCode):
    #strKey1=unicode(_strKey,'gbk')  #注意，非控制台输入，此处无须添加，此处留作记录
    params={}
    params['']=_strKey.encode(enType[_enCode])
    strKey = urllib.urlencode(params)
    #strKey = 
    return ''.join(strKey.split('=',1))
