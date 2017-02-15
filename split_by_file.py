#!/usr/bin/python  
# coding:utf8  
import os
import sys
import jieba   #导入jieba中文分词
reload(sys)
sys.setdefaultencoding("utf-8")  

#对file_list中的每个file做中文分词
def split_by_file(file_list):
    for _file in file_list:
        text = open(_file).read()
        seg_list = jieba.cut(text, cut_all=True)  
        print  "/ ".join(seg_list)  
    print("Finish searching.") 

# 返回指定目录的所有文件（包含子目录的文件）
def get_all_file(floder_path):  
    file_list = []  
    if floder_path is None:  
        raise Exception("floder_path is None")  
    for dirpath, dirnames, filenames in os.walk(floder_path):  
        for name in filenames:  
            file_list.append(dirpath + '/' + name)  
    return file_list  

basedir = raw_input("Please input the directory:") 
basedir = unicode(basedir , "utf8")    
split_by_file(get_all_file(basedir))