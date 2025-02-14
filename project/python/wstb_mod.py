#!/usr/bin/env python
#-*- coding:utf-8 -*-
#by Python2.7

import xml.dom.minidom
import wstb_encode_mod     #字符编码模块
#sys.path.append("libs")

dom = xml.dom.minidom.parse('./data_wstb.xml')
root = dom.documentElement
lisClass = []          #由于元祖值无法变更，所以，只要将可变的列表作为元祖值就可以了。
lisSearch = []
lisCoding = []         #搜索关键字编码

lisClass  = root.getElementsByTagName("category")
lisSearch = lisClass[0].getElementsByTagName('engine')

#XML文档初始化，预读取。
def _INIT_XML_(_xmlFilename):
    return

#取所选分类下的当前搜索引擎的搜索代码
def getLisCategory():
    lisClass=[]
    for nodName in root.getElementsByTagName('category'):
        lisClass.append(nodName.getAttribute('name'))
    return (lisClass)

#取搜索引擎列表
def getLisEngine(_category=0):
    lisSearch=[]
    lisText=[]
    global lisCoding
    lisCoding=[]                  #在此清空列表，否则内容会递增，编码格式名称的位置与实际不符。  20170104
    for nodName in root.getElementsByTagName('category')[_category].getElementsByTagName('engine'):
        lisSearch.append(nodName.getAttribute('name'))
        lisCoding.append(nodName.getAttribute('coding'))
        lisText.append(nodName.getAttribute('url'))
    return (lisSearch),lisText    #此处返回2个值，分别是：搜索引擎名称、搜索地址

#获取子节点列表
def Node_List(_nodename0):
    lisNode=[]
    lisNodeName=[]
    lisNode=lis_class[_nodename0].getElementsByTagName('engine')
    for name in lisNode:
        lisNodeName.append(name.getAttribute('url'))

    return lisNodeName

#地址分析
def str_read(_strAddress,_strEncode,_strKey='TEST',_strSerchkey=''):
    tem_str_url = _strAddress.split(_strKey)               #将地址字符串按关键字进行分割
    str_url = tem_str_url[0] + wstb_encode_mod.keyEncode(_strSerchkey,lisCoding[_strEncode]) + tem_str_url[1]
    return str_url

#_INIT_XML_('data_wstb.xml')

