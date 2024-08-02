"""num_str = str(11)
print(type(num_str),num_str)
#万物皆可转字符串，但是将字符串穿换成数字需要让字符串里面的东西是数字
#print（多行注释）
name = "黑马程序员"
print(type(name),name)
"""

"""#如果定义的字符串内包含着引号，看看接下来的解决方法
name = '黑马程序员“'# 外面有双引号，里面就可以用单引号，
print(name)
#使用转义字符
name1 = " 黑\"马程序员"#在前面加一个反斜杠
print(name1)"""

#字符串的拼接
print('wogenqiang'+'wohaishizuiqiang')

#字符串格式化 占位
num = 57
salary = 16647
message = ('python学习，北京%s期，毕业平均工资%s' % (num,salary))#通过拼接完成字面量和数字的拼接
print(message)

stock_price = 19.31555
number = 2222
print('我体面得很，%d坏了 今天的股价是%.3f' % (number,stock_price ))



