#!/usr/bin/env python
#-*- coding:utf-8 -*-
#by Python2.7

import xml.dom.minidom

#sys.path.append("libs")

dom = xml.dom.minidom.parse('./data_wstb.xml')
root = dom.documentElement
lisClass=[]          #由于元祖值无法变更，所以，只要将可变的列表作为元祖值就可以了。
lisSearch=[]

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
    for nodName in root.getElementsByTagName('category')[_category].getElementsByTagName('engine'):
        lisSearch.append(nodName.getAttribute('name'))
        lisText.append(nodName.getAttribute('url'))
    return (lisSearch),lisText

#获取子节点列表
def Node_List(_nodename0):
    lisNode=[]
    lisNodeName=[]
    lisNode=lis_class[_nodename0].getElementsByTagName('engine')
    for name in lisNode:
        lisNodeName.append(name.getAttribute('url'))

    return lisNodeName



#地址分析
def str_read(_strAddress,_strKey='TEST',_strSerchkey=''):
    tem_str_url = _strAddress.split(_strKey)               #将地址字符串按关键字进行分割
    str_url = tem_str_url[0] + _strSerchkey + tem_str_url[1]
    return str_url


#_INIT_XML_('data_wstb.xml')

