"""
def 函数名(传入参数):  （和C语言一样，参数和返回值均可以省略）
    函数体
    return 返回值
"""


def my_len(data):  # 自定义一个函数
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")


str1 = "iffihg"
str2 = "123456"
my_len(str1)
my_len(str2)


def printf():
    print("请出示24小时核酸阴性证明")


printf()


def check(x):
    """
    #函数的注释
    :param x: 体温
    :return: 测试一下None
    """
    if x <= 37.5:
        print("体温正常，请进")
    elif x > 37.5:
        print("需要隔离")
    else:
        print("，输入错误，请输入体温")
    return None


t = float(input("请输入您的体温"))
check(t)

# 局部变量和全局变量
num = 200


def say():
    num = 500  # 这样子不受影响
    print(num)


say()
print(num)


def said():
    global num
    num = 500


said()
print(num)


# 函数的进阶之多返回值
def text_return():
    return 1, 2, 'hello'


x, y, z = text_return()
print(x, y, z)


# 多种传入参数方式
# 位置参数
# 关键字参数
def user_info(name, age, gender):
    print(name, age, gender)


user_info(name='小米', gender='man', age=11)  # 这样子就可以不用注意形参的位置输入参数，使用于多个传入参数时


# 关键字参数和位置参数可以混用

# 缺省参数，设置一个默认参数,设置默认值时必须把形参放在最后面
def user_info(name, age=11, gender='man'):
    print(name, age, gender)


user_info('dulao')


# 不定长参数，适用于不确定需要传入多少个参数的情况
def user_infor(*args):  # 位置传递的不定长，8args是一个元组，传入的数据以元组的方式存储
    print(args)


user_info('tom', 22)


# 关键字传递不定长
def user_info(**kwargs):  # 以字典的形式存在
    print(kwargs)


user_info(name='222', age=333, gender='man')


# 函数作为参数传递,代码执行逻辑的传入
def text_func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


text_func(compute)

# 通过lambda定义匿名函数，只能使用一次的临时函数
# 语法：lambda 参数： 执行逻辑
def text_func(compute):
    result = compute(1, 2)
    print(result)
text_func(lambda x, y: x + y)
