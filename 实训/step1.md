[TOC]

---

####任务描述
[comment]: <> (“任务描述”部分需要把本关要让学生解决的问题描述的最好一句话描述清楚，并附加效果图，如：)

本关是我们的第一关，任务非常简单，只要搞清楚我们面对的数据类型是什么，并能实现数据类型之间的转换，就可以过关啦！


####相关知识
[comment]: <> (“相关知识”部分要把本关需要用到的知识点清晰，具体，简单生动的讲明白，要让学员，看得懂，记得住，能理解)

> 将要出现的函数列表：
`mod()`: 用来查看数值类型的函数；
`as.numeric()`: 将数据类型转换为数值型类型的函数；
`as.logical()`: 将数据类型转换为逻辑型类型的函数；
`as.character()`: 将数据类型转换为字符型类型的函数；


在我们开始学习R语言数据类型之前，先让我们根据例子来看看3个简单的概念。

- 定义：按照数据的格式，将数据类型发送给R。
比如定义简单的数值
<img src="/attachments/download/192662" style="display: block;height: auto;width: 100%;margin :0 auto;"/>


- 变量与赋值：与其他语言类似，变量是我们操纵数据的载体，而赋值则是数据传递给变量的一个过程。

<img src="/attachments/download/192663" style="display: block;height: auto;width: 60%;margin :0 auto;"/>

在R语言中，赋值符号有三种，分别如上图所示。大家可以根据自己的喜好选择使用~但是一般来说，大部分人都会选择中间的赋值方式，因为它更为形象。

现在我们正式开始学习R语言中的数据类型。
##### 逻辑型数据
逻辑型数据的定义方式很简单，就是直接写上 `TRUE` 或`FALSE`的大写字母即可。
**注意：R 只认大写的 `TRUE `或`FALSE`。**

它的运算规则有3种，如下图所示：
<img src="/attachments/download/192665" style="display: block;height: auto;width: 90%;margin :0 auto;"/>
我们可以通过一个例子来加深对`逻辑型数据`及运算规则的理解。

<img src="/attachments/download/192666" style="display: block;height: auto;width: 100%;margin :0 auto;"/>


从上图的执行过程中，我们能看出`x`实际上应该小于`y`的，所以当我判断`x`大于`y`的时候，你能从右边的`环境变量框`中看见，`z`的值为`FALSE`。
再检验一下，用`mod()`函数来看看`z`现在的数据类型。WALA~~结果为logical，逻辑型~

最后我们来一条一条执行逻辑型数据的运算规则，看起来很清晰明了吧~
<img src="/attachments/download/192667" style="display: block;height: auto;width: 100%;margin :0 auto;"/>




##### 数值型数据
`数值型数据`就是我们数学中学过的实数啦，包含正数、0和负数。也是我们最容易理解的数据类型了~

其中的“四则运算”，也是我们最熟悉的运算规则啦！我就不在这里多啰嗦了哟。

##### 字符型数据
在 R 中，我们把用`' '`或者`" "`包含起来的数据称为`字符型数据`。
让我们来看看`字符型数据`是什么样子的，以 hello world 为例，嘿嘿。
<img src="/attachments/download/192668" style="display: block;height: auto;width: 100%;margin :0 auto;"/>

恩，看来没错，`mode()`函数告诉我们，`x`和`y`都是`character` `字符型`变量。

##### 数据间的转换
R 语言数据类型的转换很“显式”，因为它是通过函数做到的，不会出现一不小心就被默认转换坑了的情况，不要问我是怎么知道的...
<img src="/attachments/download/192669" style="display: block;height: auto;width: 90%;margin :0 auto;"/>

举个例子来看看`逻辑型数据`转成`数值型数据`是怎么做的吧。
<img src="/attachments/download/192670" style="display: block;height: auto;width: 100%;margin :0 auto;"/>


那么问题来了，`字符型数据`是否能转换为`数值型数据`呢？哈哈，好奇害死猫，我不告诉你，快去自己试试吧。

####编程要求
[comment]: <> (“编程要求”部分说一下本关要解决的问题的具体要求，并给出相应代码的框架，以及要求学生填写的那一块)

你的任务是：根据我的代码注释，把已有的数据类型转换成另一种数据类型，方法已经告诉你了，开始吧~


####测试说明
程序会对你编写的代码进行测试：

比如`数值型数据`转换为`字符型数据`：输入测试数据：`1`，需要你的程序输出：`"1"`

---
开始你的任务吧，祝你成功！

<img src="/attachments/download/192671" style="display: block;height: auto;width: 30%;"/>
