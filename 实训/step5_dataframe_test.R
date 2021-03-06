#建立一个两列的数据框，列名分别为 ”x“ 和 ”y“ , 并输出该数据框
# x 的元素是 c(1,2,3,4,5),y 的元素是 c(2,4 6 8 10)
d <- data.frame(x=c(1, 2, 3 ,4, 5), y=c(2, 4, 6, 8, 10))
d

#查看该数据框结构
str(d)

#以非向量的形式读出数据框的 x 列 
d[, c("x"), drop=FALSE]

#将数据框中 x 列的值由1，2，3，4，5换成6，7，8，9，10，并输出数据框
d$x <- 6:10
d

#再往该数据框中添加新列 ”z“，包含元素”A“,"B","C","D","E", 并输出新的数据框

d$z <- c("A","B","C","D","E")
d

#用运算符 %in% 输出 y、z 列 与第一、二行
d[c(1,2), !names(d) %in% c("x")]
