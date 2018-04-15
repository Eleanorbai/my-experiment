#创建一个列表，该列表有4个对象，分别是g、h、j、k
#其中对象 g 的 name 为 title，对象 h 的 name 为 ages，其他对象没有 name
#g 为 标量字符串“My First List”
#h 为数值向量，包含元素 25，26，18，39
#j 为 5*2 的矩阵，元素为1：10
#k 为字符串向量，包含元素 “one”，“two”，“Three”
#输出该列表
g <- "My First List"
h <- c(25, 26, 18, 39)
j <- matrix(1:10, nrow=5)
k <- c("one", "two", "Three")

mylist <- list(title=g, ages=h, j, k)
mylist

#输出该列表的第二个对象的 value
mylist[[2]]

#输出该列表第三个对象
mylist[3]


#输出“ages”的value
mylist[["ages"]]