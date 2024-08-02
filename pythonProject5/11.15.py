sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print('1-100累加的和是%d ' % sum)

#九九乘法表
i = 1
j = 1
while i<= 9:
    while j <= 9:
        if j>= i:
            print('%d*%d=%-3d' % (i,j,i*j))
        else:
            print('       ')
        j += 1
    print('\\n')

i += 1