# -*- coding: utf-8 -*-
"""
本文件通过类将阿拉伯数字实例化，得到相对应的罗马数字。
"""

class NumToRomanNum:      #创建一个NumToRomanNum类
    def __init__(self, num):      #构造函数，初始化属性num
        self.num = num
    
    def transform(self):      #定义一个transform()方法,将阿拉伯数字转化为罗马数字
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X",\
                      "IX", "V", "IV", "I"]
        roman_num = ""
        if self.num <3999:
            for i in range(len(num_list)):
                while self.num >= num_list[i]:
                    self.num -= num_list[i]
                    roman_num += roman_list[i]
            return roman_num