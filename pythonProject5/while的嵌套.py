i = 1
flag = True
while flag:
    print("今天是第%d天，准备干大事" % i)
    j = 1
    while j <= 10:
        print('送给王小美%d朵玫瑰花' % j)
        j += 1
    print("小美我喜欢你")
    answer = input('你喜欢我吗')
    if answer == '不喜欢':
        i += 1
        print('没关系，我会努力的')
    elif answer == '喜欢':
        flag = False
    else :
        print('没听懂当你默认了')
        flag = False
print(f'坚持到第{i - 1}天,表白成功')
