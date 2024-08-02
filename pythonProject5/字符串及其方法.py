# 下标索引
mystr = 'ithiema and it cast'
value = mystr[2]
print(value)

# 字符串不支持修改

# index方法
value = mystr.index('and')
print(value)

# replace方法
# 语法 字符串.(1, 2)，将字符串1替换为字符串2，是得到了一个新字符串
newstr = mystr.replace('it', '程序')
print(newstr, mystr)

# .split 分隔字符串，将指定的分隔字符串，存入列表对象，字符串本身不变，而是得到了一个列表对象
mystr = 'helllo python itheima'
mystr_list = mystr.split()  # 用空格进行分隔
print(mystr_list, mystr)

# 规整操作（去除前后指定的字符串）.strip() 如果不传入参数则是去掉开头和结尾的空格或者换行符
mystr = "  itheima and itcast  "
print(mystr)
print(mystr.strip())
mystr = '12itheima21'
print(mystr)
print(mystr.strip('12'))

# 统计元素出现个数count
# 计算字符串长度len

mystr = 'itheima itcast boxuegu'
num = mystr.count('it')
newstr = mystr.replace(' ', '|')
newstr_list = newstr.split('|')
print(f"{mystr}中it的个数是{num}")
print(f"{mystr}中的空格被替换成|后{newstr}")
print(f"{newstr},安照|进行分隔后{newstr_list}")
