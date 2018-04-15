[TOC]

---

####任务描述
[comment]: <> (“任务描述”部分需要把本关要让学生解决的问题描述的最好一句话描述清楚，并附加效果图，如：)
在挑战这一关之前，我会介绍 R 语言中的数据框，也会顺便介绍一些常用的功能函数。然后，就轮到你来亲自上手，简单操作一下这些数据结构了哟，需要使用到的函数都在下面的相关知识里~而我想让你完成什么任务呢？请看右边的代码注释。
<img src="/attachments/download/192637" style="display: block;height: auto;width: 20%;"/>


####相关知识
[comment]: <> (“相关知识”部分要把本关需要用到的知识点清晰，具体，简单生动的讲明白，要让学员，看得懂，记得住，能理解)
> 本节将要用到的函数：
data.frame(): 用来建立数据框的函数
str(): 查看数据框结构



##### 数据框
![](/attachments/download/193452)

由于不同的列可以包含不同模式（数值型、字符型）的数据，数据框的概念跟矩阵相比更为一般。

> 数据框将是你在 R 中最常处理的数据结构。

![](/attachments/download/193460)

给你们看个秘密，这是 educoder 平台上的实训数据，嘘。。。
你看，这个表里包含了数值型和字符型数据，我们没有办法为它建一个矩阵，所以，这种情况下，数据框是最好的选择。

**创建数据框：**
数据框可以通过函数**`data.frame(col1, col2, col3, ...)`**来创建。
其中列向量`col1`,`col2`,`col3`可为任何类型。

> 每一列数据的模式必须唯一，不过你却可以将多个模式的不同列放到一起组成数据框。

比如执行以下代码后：
```R
patientID <- c(1, 2, 3, 4)
age <- c(25, 34, 28, 52)
diabetes <- c("type1", "type2", "type1", "type1")
status <- c("Poor", "Improved", "Excellent", "Poor")
patientdata <- data.frame(patientID, age, diabetes, status)
patientdata
```
我们能得到结果：
![](/attachments/download/193472)



###### 如何访问数据框中的数据
我们可以像之前一样使用索引来访问数据框中的元素，也可以用数据框特有的新办法来访问，那就是`$`符号。
举个例子来看看吧：
```R
patientdata[1:2]
```
得到的结果是：
![](/attachments/download/193476)

```R
patientdata[c("diabetes", "status")]
```
得到的结果是：
![](/attachments/download/193478)

```R
patientdata$age
```
得到的结果是：
![](/attachments/download/193479)

`$`符号被用来选取一个给定数据框中的某个特定变量。它还有个很好用的用法，就是通过符号`$`，我们可以用列名做联表！
![](/attachments/download/193485)

我们也可以将不存在的列`w`，添加到数据框`patientdata`上。
```R
patientdata$w <- c("A", "B", "C", "D")
```


###### 数据框中常用的函数
1. 使用函数`str()`可以查看数据框结构，可以轻松得知各列保存着哪种类型的数据。比如查看我们刚才用过的糖尿病人的数据结构：
![](/attachments/download/193495)
从结果可以看出，`diabetes`列和`status`列都是因子（factor）列。因子我们会在下一节中讲到~

2. `names()`函数用于返回数据框点的列名。使用 `%in%`运算符与`names()`函数，能够快速选取特定列。
比如：数据框 b 拥有 a、b、c三个列，使用
```R
d[ ,names(d)%in%c("b","c")]
```
![](/attachments/download/193506)
只选取并输出b、c列。

反之~使用`!`运算符可以排除特定列，很好用哇~
![](/attachments/download/193515)

我们就这样得到了列`a`。细心的同学可能要喊不对了~怎么列`a`变成了向量呢，我的数据框呢？
这是因为，列是一维时，返回值与相应列的数据类型不同。想避免这种类型转换的话，只需要设置`drop=FALSE`即可：
![](/attachments/download/193522)

####编程要求
[comment]: <> (“编程要求”部分说一下本关要解决的问题的具体要求，并给出相应代码的框架，以及要求学生填写的那一块)

按照右边代码中的注释来完成任务哟~



---
开始你的任务吧，祝你成功！
<img src="/attachments/download/193069" style="display: block;height: auto;width: 40%;"/>

