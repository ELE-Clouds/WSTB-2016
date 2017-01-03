#coding:utf-8
from distutils.core import setup
import py2exe

lisFiles = ["data_wstb.xml","wstb.ico"]

options = {"py2exe":{
	"optimize":2,
	"bundle_files":3
}}
setup(
	options = options,  
    zipfile=None,  
    name = "快捷搜索工具栏",  
    description = "集成各搜索引擎的输入框，确认后即会弹出当前选定搜索引擎进行搜索。",     
	author="Robin Chen",
	windows = [{
	"script": "wstb_gui.pyw",
	"icon_resources": [(1, "wstb.ico")]}],
	data_files = [ ( "", lisFiles )] 
	)