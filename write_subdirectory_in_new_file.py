import os
# coding:utf8 

# 写入中英文字符串到文件的方法
import codecs

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

basedir = raw_input("Please input the directory:") 
basedir = unicode(basedir , "utf8")  

f = codecs.open('filelist.txt', 'w')
# os.walk 中 
# dirpath 是一个string，代表目录的路径；
# dirnames 是一个 list，包含了dirpath下所有子目录的名字；
# filenames是一个list，包含了非目录文件的名字
for dirpath, dirnames, filenames in os.walk(basedir):
#写入每一个子目录的名字
    f.writelines(dirnames)
    f.writelines("\n")

f.close()