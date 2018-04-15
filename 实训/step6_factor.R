#读取学生在作业1737中的表现
choice <- read.csv('user_choice_1737.csv')

#查看数据框choice的数据结构


#学生们的选择题答案存在了choice_position列里，查看choice_position里的因子水平名称


#choice_position里的因子水平分别是A，B，C，D，但是选B选项的人最多
#请按B，A，C，D的顺序给因子水平排序，并输出choice$choice_position
choice$choice_position <- 

