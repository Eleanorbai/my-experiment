# coding=utf-8
import os, sys
import os.path
import jieba
import re
import datetime,codecs
reload(sys)
sys.setdefaultencoding('utf-8')

PATH = "/Users/eleanor/陈立前老师题库/陈立前老师提供的题库--20170208/全部试题765"
#upath = unicode(PATH, 'utf-8')
upath=PATH
#CODEC = 'utf-8'
result_dict={}
dict={}
num=1
dictName="dict"
sortFileName="sort.txt"
nosortFileName="nosort.txt"
sort={}
nosort=[]
def getFileChinese(filePath):
	file = open(filePath)
	str = file.readlines()
	newStr=""
	for i in range(0,len(str)):
		# print str[i]
		newStr += str[i].decode('gbk').encode('utf-8')
	newStr=unicode(newStr, 'utf-8')
	strs = re.findall(ur'[\u4e00-\u9fa5]',newStr)
	chinese=''
	for i in range(0, len(strs)):
		# for j in range(0,len(str[i])):
		chinese+=strs[i]

	return chinese

def getDesFile():
	resultFile=codecs.open(os.path.join(upath,"result.txt"),'w');
	noresultFile=codecs.open(os.path.join(upath,"noresult.txt"),'w');
	for dirname in os.listdir(upath):
		newDir = os.path.join(upath, dirname)
		if not os.path.isdir(newDir):
			continue
		for dirname2 in os.listdir(newDir):
			newDir2 = os.path.join(newDir, dirname2)
			if not os.path.isdir(newDir2):
				continue
			is_describe=False
			for dirname3 in os.listdir(newDir2):
				if dirname3.split(".")[0] == "试题描述":
					filePath= os.path.join(newDir2,dirname3)
					try:
						string=getFileChinese(filePath)
						seg_list = jieba.cut(string, cut_all=False)
						is_describe=True
						resultFile.write(os.path.join(dirname,dirname2))
						resultFile.write('\n')
						keyList=[]
						for one in list(seg_list):
							# print one
							resultFile.write(one+'\t')
							keyList.append(one)
						resultFile.write('\n***\n')
						result_dict[os.path.join(dirname,dirname2)]=keyList
					except Exception,e:
						print Exception
						print filePath
			if not is_describe:
				noresultFile.write(os.path.join(dirname,dirname2)+'\n')
	noresultFile.close()
	resultFile.close()

def get_dict():
	for i in range(num):
		filePath=os.path.join(upath,dictName+str(i+1)+'.txt')
		filePath=filePath.encode('utf-8')
		file=codecs.open(filePath,'r')
		dict_str=file.readlines()
		one_dict=[]
		for one in dict_str:
			tmp=one.strip()
			one_dict.append(tmp)
		dict[i]=one_dict
		file.close()


def match():
	# print dict
	# print result_dict
	for (d,x) in dict.items():
		problem=[]
		for (p_num,p_key) in result_dict.items():
			isSort=False
			for one in x:
				for two in p_key:
					if one==two:
						print one,two
						problem.append(p_num)
						isSort=True
						break
				if  isSort:
					break
				else:
					nosort.append(p_num)
		sort[d]=problem

def saveResult():
	sortFile=codecs.open(os.path.join(upath,sortFileName),'w','utf-8');
	nosortFile=codecs.open(os.path.join(upath,nosortFileName),'w','utf-8');
	for one in nosort:
		nosortFile.write(one+"\n")
	for (d,x) in sort.items():
		sortFile.write(str(d))
		sortFile.write("\n")
		for one in x:
			sortFile.write(one+"\n")
		sortFile.write("\n")
	sortFile.close()
	nosortFile.close()
if __name__ == '__main__':
	getDesFile()
	get_dict()
	match()
	saveResult()
