# 定义字典
# {key: value, key: value}

my_dict = {'王力宏': 99, '周杰伦': 88, 'ljj': 77}
my_dict2 = dict()  # {}也可以

# 字典中的key是不可以重复的

# 字典也不可以使用下标索引
# 使用方法

score = my_dict['王力宏']
print(score, type(score))

# 字典的key和value可以是任何数据，也就是说可以嵌套
mydict = {'王力宏': {'math': 66, 'chinese': 77, 'english': 33}, '周杰伦': {'math': 86, 'chinese': 88, 'english': 55}}
print(mydict['王力宏']['math'])

# 常用操作
# 新增元素和更新元素语法一样 字典[key]=value 如果没有这个key值就是新增
mydict['王力宏']['math'] = 55
print(mydict)
mydict['张信哲'] = {'math': 11, 'chinese': 11, 'english': 11}
print(mydict)

# 删除.pop(key)
mydict.pop('周杰伦')
print(mydict)

# 清空元素.clear（）

# 获取全部key的操作 字典.keys(), 得到字典中全部的keys，用来写字典的遍历
keys = mydict.keys()
# 遍历
for i in keys:
    print(mydict[i])
for i in mydict:
    print(mydict[i],i)

# 统计字典的元素数量len()

memberdict = {'王力宏': {
                  '部门': '科技部',
                  '工资': 3000,
                  '级别': 1
              },
              '周杰伦': {
                  '部门': '市场部',
                  '工资': 5000,
                  '级别': 2
              },
              '林俊杰': {
                  '部门': '市场部',
                  '工资': 7000,
                  '级别': 3
              },
              '张学友': {
                  '部门': '科技部',
                  '工资': 4000,
                  '级别': 1
              },
              '刘德华': {
                  '部门': '市场部',
                  '工资': 6000,
                  '级别': 2
              }
             }
for key in memberdict:
    if memberdict[key]['级别'] == 1:
        memberdict[key]['级别'] = 2
        memberdict[key]['工资'] += 1000
    else:
        continue
print(memberdict)
