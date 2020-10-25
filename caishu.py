import random
x=random.randint(0,100) #产生一个0~100的随机整数
i=0
while True:
    y=input("输入一个100以内的整数：")
    y=eval(y) #将数据类型转换为int
    if y>100 or y<0:
        print("输入数字超出范围，请重新输入：")
        y=eval(input())
    i=i+1
    if y==x:
        print("猜测正确！共猜测"+str(i)+"次。")
        break
    else:
        print("猜测错误！")