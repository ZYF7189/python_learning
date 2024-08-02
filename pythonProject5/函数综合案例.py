name = input("请输入您的名字")
money = 5000000
def menu():
    print("-----------主菜单----------")
    print(f"{name}您好,欢迎来到ATM,请选择操作")
    print("查询余额  【输入1】")
    print("存款     【输入2】")
    print("取款     【输入3】")
    print("退出     【输入4】")
def detect():
    print(f"{name}您好，您的存款为{money}")
def save_money():
    num = int(input("请输入您的存款数目"))
    global money
    money += num
    print(f"{name}您好，您已存款成功{num}元，当前余额为{money}元")
def get_money():
    num = int(input("请输入您的取款数目"))
    global money
    money -= num
    print(f"{name}您好，您已取款成功{num}元，当前余额{money}元")
flag = True
while flag:
    menu()
    print()
    order = int(input())
    if order == 1:
        detect()#查询余额函数
    elif order == 2:
        save_money()
    elif order == 3:
        get_money()
    elif order == 4:
        print("本次使用已结束，感谢您对本银行的支持")
        flag = False
    else:
        print("输入错误，请重新开始，若无法解决请联系工作人员！！！")
        flag = False

