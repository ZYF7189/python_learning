# 集合使用{}，关键字是set，集合是无序的，不能有重复元素
myset = {'黑马程序员', 'itheima', 'python', '黑马程序员'}
print(myset)  # 不能使用索引

# add添加新元素
myset.add('PYTHON')
print(myset)

# 移除元素
myset.remove('黑马程序员')
print(myset)

# 随机取出一个元素
myset = {'深圳大学', 'python', '电子与信息工程学院'}
element = myset.pop()  # 随机取出
print(element)
print(myset)

# 清空集合.clear

# 取两个集合的差集 集合1.difference（集合2）：取出集合1有而集合2没有的
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set3, set1, set2)

# 消除差集：集合1.difference_update(集合2) 删除集合1中和集合2相同的元素
set1.difference_update(set2)
print(set1)

# 合并集合：集合1.unior(集合2)得到新集合
set3 = set1.union(set2)
print(set3)

# 统计集合元素数量 len

# 集合的遍历只能用for循环，因为while循环的本质是利用索引

mylist = ['黑马程序员', 'beijing', '黑马程序员', 'beijing', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
myset = set()
for i in mylist:
    myset.add(i)
print(myset)