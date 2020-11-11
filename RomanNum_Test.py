# -*- coding: utf-8 -*-
"""
本文件是NumToRomanNum类的测试文件。
"""

from numToRomanNum import NumToRomanNum
import sys

num = input("请输入一个阿拉伯数字：")
if not num.isdigit():
    print(f"请输入一个正整数！")
    sys.exit(1)      #程序退出
obj = NumToRomanNum(int(num))
print(f"{num}对应的罗马数字是{obj.transform()}。")