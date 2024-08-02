name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_daillygrowth = 1.2
day = 7
print(f"公司：{name},股票代码{stock_code},当前股价{stock_price}")
print("每日增长系数是%.2f,经过%d天的增长，股价达到了：%.3f" % (stock_daillygrowth,day,(1.2**7)*19.99) )