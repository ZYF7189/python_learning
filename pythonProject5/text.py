#print("i love you")

#temp = input("不妨猜一下小甲鱼心里想的是哪个数字：")
#guess = int (temp)
#if guess==8:
 #   print("我草你是小甲鱼心里的蛔虫吗")
   #  print("猜中了也没有奖励")
#else:
 #   print("猜错了，小甲鱼现在心里想的是8！")
#print("游戏结束，不玩啦^_^")

#help(eval)

#temp = input("请输入你的姓名：")
#print("你好"+temp)

#favourite = 'Fishc'
#for i in favourite:
    #print(i,end=' ')

member=['小甲鱼','老甲鱼','大鲨鱼']
member.append('福禄娃娃')#添加元素
member.extend(['1','2'])#一次高进多个参数
member.insert(0,'牡丹')#insert(1,'参数')填入位置
#while True:
    #print(member[1])0
member.remove(member[3])
del member[0]
member.pop()
print(member)

list1=[1,5,66,8,7,9]
list2=list1[2:]#列表切片
print(list2)

