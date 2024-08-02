# index函数
mylist = ['itheima', 'itcast', 'python']
index = mylist.index('itheima')
print(f"itheima的索引值是{index}")

# 修改指定下标位置的值
mylist[1] = '555'
print(f"修改后的列表为{mylist}")

# 元素的插入，列表.insert(下标，元素)，在指定的下标位置，插入指定的元素
mylist.insert(3,'要插进去了')
print(f"使用了insert函数后为{mylist}")

# append方法，只能插入到尾部
mylist.append('插到后面')
print(f'使用了append语句后为{mylist}')

# 在尾部传入一串元素extend，将其他数据容器的内容取出，依次追加到列表尾部
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f'用extend追加一个新的列表后{mylist}')

# 元素的删除 del列表【下标】 列表.pop(下标）
del mylist[2]
mylist.pop(1)
print(f'用了删除语句后为{mylist}')

# 不用下标直接删除内容
mylist.insert(0,'itcast')
mylist.insert(2,'itcast')
mylist.remove('itcast')
print(f"使用remove方法后为{mylist}")

# 计算列表里元素的数量
mylist.insert(0,'itcast')
count = mylist.count('itcast')
print(f'{mylist}中itcast的数量是{count}')

# 计算元素的数量
count1 = len(mylist)
print(f'{mylist}中的元素有{count1}个')

# 清空列表.clear
mylist.clear()
print(f'清空后的列表{mylist}')