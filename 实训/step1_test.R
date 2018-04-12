#将 “3.14” 赋值给变量 pi，并查看 pi 的数据类型
#注意！是带引号的 3.14
#----start----
pi <- '3.14'
mode(pi)
#-----end-----


#将 pi 的数据类型转换为数值型，并查看转换后 pi 的数据类型
#注意！是转换后的数据类型
#----start----
pi <- as.numeric(pi)
mode(pi)
#-----end-----

#将 t 的数据类型转换为数值型,并输出 t 的值
t <- 'TRUE'
#----start----
t <- as.logical(t)
t <- as.numeric(t)
t
#-----end-----

