# -*- coding: utf-8 -*-
"""
本文件运用循环语句、生成器、迭代器三种方法实现斐波那契数列。
"""
import sys
import numpy as np

def fib_loop(n):
    num_zero = 0      #初始化第0项为0
    num_one = 1      #初始化第1项为1
    print(f"斐波那契数列前{n}项为：", end = "")
    for i in range(n):
        print(f"{num_zero}  ", end = "")
        #前两项为0，1，其后每一项等于前两项之和    
        num_zero, num_one = num_one, num_zero + num_one      
    return


def fib_yield(n):
    num_zero = 0
    num_one = 1
    print(f"斐波那契数列前{n}项为：", end = "")
    for i in range(n):
        yield num_zero      #生成器关键字
        num_zero, num_one = num_one, num_zero + num_one


def fib_matrix(n):
    num_zero = 0
    num_one = 1
    print(f"斐波那契数列前{n}项为：{num_zero}  ", end = "")
    for i in range(n-1):
        #矩阵[[Fn],[Fn-1]]=[[1, 1], [1, 0]]^(n-1)*[[F1], [F0]]
        result = pow(np.matrix([[1, 1], [1, 0]]), i) *\
        np.matrix([[num_one], [num_zero]])
        print(f"{int(result[0][0])}  ", end = "")


def default(n):
        print("没有此方法！循环语句法请输1，生成器法请输2，迭代器法请输3！")


switch = {'1': fib_loop,      #以字典形式实现switch功能
          '2': fib_yield,
          '3': fib_matrix,
          }
n = input("请输入需要的斐波那契数列项数：")
if not n.isdigit():
    print("输入错误！项数必须为正数！")
    sys.exit(1)     #程序退出
choice = input("请选择方法，循环语句法请输1，生成器法请输2，迭代器法请输3：")
obj = switch.get(choice, default)(int(n))      #执行相应函数，否则执行default函数
if choice == '2':
    for index in obj:
        print(f"{index}  ", end = "")      #从生成器对象obj中提取