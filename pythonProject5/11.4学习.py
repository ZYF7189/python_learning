print("heimacxuyuan")
print(666)
"""现在在写多行注释，测试
"""
# 单行注释，前面加空格比较规范
# 变量
money = 50
print("钱包还有：",money)# ,是用来隔开多份输出数据的

# 使用type数据类型

str_type = type("坏事")
int_type = type(666)
float_type = type(6.23)
print(str_type,int_type,float_type)

#数据类型的转换
"""
语句（函数）int（x），将x转换为整数
            float，转换成浮点数
            str转换成字符串
"""
num_str = str(11)
print(type(num_str),num_str)
#将字符串转换成整数,将字符串穿换成数字需要字符串里面的内容都是数字
数字 = int("11")
float_num = float("11")
print(type(数字),数字,float_num)

#运算符,一个比较特别的是**是幂运算，C语言中是没有的
print("11//2=",11//2)
print("2**3=",2**3)

#字符串的拓展
#字符串可以用单引号，双引号来定义
#在字符串内包含单引号或双引号
