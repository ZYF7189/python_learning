# 只能读取，不能篡改
#(元素，元素)， tuple()
t1 = ((123), (1, 11), 1, 2, 3, 2) #也可以嵌套

# 索引取出
print(t1[1][1])

# 计算某个元素出现的次数
num = t1.count(2)
print(num)

# 也可以通过while和for循环遍历

# 但是在元组中的列标是可以修改的
t2 = (1,2,3,[15,66,89])
t2 [3][2] = 66
print(t2)
t2[3].clear()
print(t2)

t = ('周杰伦', 11, ['football', 'music'])
index = t.index(11)
print(index)
t[2].remove('football')
t[2].append('coding')
print(t)
