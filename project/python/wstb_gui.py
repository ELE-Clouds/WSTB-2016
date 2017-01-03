#!/usr/bin/python
# -*- coding: UTF-8 -*-
#by Python2.7

import Tkinter as tk
import ttk as ttk
import webbrowser
import wstb_mod    #XML文件操作模块


win = tk.Tk()
win.resizable(0, 0)
lis_Files=['./data_wstb.xml','./wstb_mod.py','./wstb_encode_mod.py']
lisUrl=[]    #网址列表


#界面布局、文件完整性检查
def _INIT_():
    if not _FileIntegrityCheck(lis_Files):
        exit()       #如果文件缺失，则退出程序。
    return

#文件完整性检查
def _FileIntegrityCheck(lisFiles):
    boolFiles = True
    for filename in lisFiles:
        '''
        boolFiles = boolFiles and path.exists(filename)
        boolFiles = boolFiles and path.isfile(filename)
        boolFiles = boolFiles and access(filename,R_OK)
        '''
        try:
    	    with open(filename) as f:
    		    boolFiles = True
        except IOError:
    	    boolFiles = False
        if boolFiles == False:
            print '文件或路径（' + filename + ')不存在，请核实后重新启动！'
    return boolFiles

#搜索关键字
def search(_strUrl,_strKey):
    webbrowser.open( wstb_mod.str_read(_strUrl,engineChosen.current(),'TEST',_strKey))
    return


#键盘事件
def evKey(event):
    search(lisUrl[engineChosen.current()],name.get())
    return


#下拉列表框点击后的事件
def catSelcomb(event):
    lis1 = ([])  #引擎
    lis2 = []    #地址
    global lisUrl
    lis1,lis2 = wstb_mod.getLisEngine(categoryChosen.current())
    engineChosen['values'] = lis1
    lisUrl = lis2
    engineChosen.current(0)
    return



#下拉列表框点击后的事件
def engSelcomb(event):
    #wstb_mod.getLisEngine(True,engineChosen.current())
    return



#def getNodeName():


#管理
#def manages():

#在输入框进行输入时对管理符号进行判断
#def change():

_INIT_()        #初始化程序，主要用于检查软件文件完整性。

win.title("搜索引擎快捷工具栏 - 2016")

# 创建一个下拉列表,搜索分类
category = tk.StringVar()
categoryChosen = ttk.Combobox(win,width=10,textvariable=category)
categoryChosen['values']=wstb_mod.getLisCategory()    #('默认','标准','视频')
categoryChosen['state']='readonly'
categoryChosen.bind('<<ComboboxSelected>>',catSelcomb)
categoryChosen.grid(column=0,row=0)
categoryChosen.current(0)

# 创建一个下拉列表，搜索引擎
engine = tk.StringVar()
engineChosen = ttk.Combobox(win,width=15,textvariable=engine)
engineChosen['values'],lisUrl=wstb_mod.getLisEngine()   #('百度','谷歌','搜狐','一搜'),当前函数返回两个值。
engineChosen.bind('<<ComboboxSelected>>',engSelcomb)
engineChosen['state']='readonly'
engineChosen.grid(column=1,row=0)
engineChosen.current(0)

# 文本框
name = tk.StringVar()
nameEntered = ttk.Entry(win,width=50,textvariable=name)
nameEntered.bind('<Key-Return>',evKey)    #键盘事件，若有按键按下，则执行evKey函数。
nameEntered.grid(column=2,row=0)
nameEntered.focus()


win.mainloop()
