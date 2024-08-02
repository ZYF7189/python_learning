print('Hello', end=' ') #后面加入 end=' '可以达到不换行的目的
print(' World')
print('hello\tworld')
print('itestm\tghji')

i = 1
while i <= 9:
    j = 1
    while j < i:
        print(f"{j}*{i}={j*i}\t", end=' ')
        j += 1
    if j == i:
        print(f"{j}*{i}={j*i}")
    i += 1
    #换行可以通过print()打印空内容实现

#用for循环
k = 1
for l in range(1,10):
    j = 1
    for m in range(1,k+1):
        print(f"{j}*{k}={j * k}\t", end=' ')
        j += 1
    print()
    k += 1
#改良版
for a in range(1,10):
    for b in range(1,a + 1):
        print(f"{b}*{a}={b * a }\t", end=' ')
    print()