# -*- coding: utf-8 -*-
"""
本文件用于生成服从几种常见概率分布的数据，并计算数据的均值、极值、方差等统计量。
"""

import numpy as np
from scipy import signal
import sys

choice = input("请选择数据服从的分布（二项分布输1，泊松分布输2，\
               均匀分布输3，正态分布输4，指数分布输5）：")

if choice == '1':
    #二项分布，n为试验次数，prob为试验成功的概率，size为重复做二项试验的次数
    n, prob, size = 10, 0.8, 50
    data = np.random.binomial(n, prob, size)
    
elif choice == '2':
    #泊松分布，lamda为一段固定时间间隔内事件发生的次数，size为重复做泊松试验的次数
    lamda, size = 5, 40
    data = np.random.poisson(lamda, size)
    
elif choice == '3':
    #均匀分布，low为数据分布下限，high为数据分布上限，size为样本个数
    low, high, size = 2, 20, 60
    data = np.random.uniform(low,high,size)
    
elif choice == '4':
    #正态分布，mu为均值，sigma为标准差，size为样本个数
    mu, sigma, size = 0, 1, 100
    data = np.random.normal(mu, sigma, size)

elif choice == '5':
    #指数分布，lamda为每单位时间内发生某事件的次数，size为样本个数
    lamda, size = 0.25, 50
    data = np.random.exponential(lamda, size)

else:
    print(f"输入无效！")
    sys.exit(1)

mean = np.mean(data)      #均值
greater = data[signal.argrelextrema(data, np.greater)]      #极大值
less = data[signal.argrelextrema(data, np.less)]      #极小值
var = np.var(data)      #方差
maximum = np.max(data)      #最大值
minimum = np.min(data)      #最小值

print(f"均值为{mean}，极大值为{greater}，极小值为{less}，方差为{var}，\
      最大值为{maximum}，最小值为{minimum}。")