#name = input("请告诉我你是谁")#可以直接在input里面输入提示语
#print("我知道了，你是%s" % name)

#输入数字时
num = input("请输入你的银行卡密码")#input总是把输入的东西转换成字符串
num = int (num)
type_1 = type(num)
print("你的银行卡类型是",type_1)

#小作业
user_name = input()
user_type = input()
print("您好，%s，您是尊贵的：%s用户，欢迎您的光临" % (user_name,user_type))