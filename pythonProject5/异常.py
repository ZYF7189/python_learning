# 基本捕获语法
try:
    f = open('D:/abc.txt', 'r', encoding="UTF-8")
except:
    print('出现了异常，文件不存在，将会以write方式打开')
    f = open('D:/abc.txt', 'w', encoding="UTF-8")

# 捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)
# 捕获多个异常
try:
    1 / 0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义异常 或者 除以0异常")
