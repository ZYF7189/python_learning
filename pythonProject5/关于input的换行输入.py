student_num = int(input())#换行输入
each_num = int(input())
print(f"{each_num*student_num}")

#不换行
student_num, each_num = map(int, input().split())
print(each_num * student_num)

text = input()
reversed_text = ''.join(reversed(text))
print(reversed_text)
