# r是只读，w是新建，a是追加
f = open("D:/测试.txt", "r", encoding='UTF-8')  # encoding参数只能使用关键字传参
print(type(f))
# read()方法
# print(f"读取十个字节的结果：{f.read(10)}")
# print(f"读取全部内容的结果：{f.read()}")# 如果在文件中多次使用read是从上一次使用read的地方继续
print("-----------------------------")

# readlines()读取文件的全部行并封装到列表中
# lines = f.readlines()
# print(f"lines的类型是：{type(lines)}")
# print(f"lines的内容是{lines}")

# readline()是只读取一行数据
# print(f.readline())
# print(f.readline())

# for循环读取文件行
for line in f:
    line = line.strip() # 去除换行符
    print(f"每一行line对象:{line}")

# 文件的关闭close()
import time

# time.sleep(5)
f.close()

# with open语法
# with open(文件对象的名称) as f:
# 缩进，自动地关闭文件


# 进行写的操作，如果文件不存在会自己创建一个文件
f = open("C:/Users/Lenovo/Desktop/测试2.txt", "w", encoding='UTF-8')

# write的写入
f.write('hello world')
f.flush() # 刷新
f.close() # close功能已经内置了flush，所以说不调用flush也是可以完成写入的


# 文件存在时会吧文件清空再覆盖
f = open("C:/Users/Lenovo/Desktop/测试2.txt", "w", encoding='UTF-8')
f.write('黑马程序员')
f.close()

# 文件追加操作，既不需要覆盖文件中的内容
f = open("C:/Users/Lenovo/Desktop/测试2.txt", "a", encoding='UTF-8')
f.write("学python的最佳选择") # 这样是连在一起的
f.write("\n月薪过万") # 实现换行
f.close()