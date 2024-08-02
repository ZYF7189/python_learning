#a=int("5")
#print(a)
#while True:
 #   try:
  #      a, b = map(int, input().split())
   #     # 计算和并输出
    #    print(a + b)
    #except EOFError:
     #   break

#while True:
    #try:
     #   a, b = map(int, input().split())
      #  print(a + b)
    #except:
     #   break

n = int(input())
result=[]
for i in range(2000,n+1):
    if i % 7==0 and i%5 != 0:
        result.append(str(i))
print(",".join(result))