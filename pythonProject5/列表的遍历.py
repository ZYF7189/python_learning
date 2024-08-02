mylist = [1, 2, 3, 4]
index = 0
while index < len(mylist):
    print(mylist[index])
    index += 1
for i in mylist:
    print(i)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
index = 0
while index < len(list1):
    if list1[index] % 2 == 0:
        list2.append(list1[index])
    index += 1
print(list2)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for element in list1:
    if element % 2 == 0:
        list2.append(element)
print(list2)