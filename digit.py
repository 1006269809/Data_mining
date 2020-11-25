# -*- coding: utf-8 -*-
"""
本文件利用朴素贝叶斯分类实现手写数字识别
"""

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

digits = load_digits()

x = digits.data     #样本
y = digits.target     #标签

#划分训练集、测试集，其中测试集的比例为0.3
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

"""高斯贝叶斯分类器：GaussianNB"""
gnb = GaussianNB().fit(x_train, y_train)     #利用训练集数据训练模型
gnb_predict = gnb.predict(x_test)     #对测试集进行预测
for i in range(10):     #输出前十个预测结果与实际结果进行比对
    print(f"actual:{y_test[i]},predict:{gnb_predict[i]}")
    gnb_score = gnb.score(x_test, y_test)
print(f"accuracy(GaussianNB):{gnb_score}")


print("-------------------")


"""多项贝叶斯分类器：MultinomialNB"""
mnb = MultinomialNB().fit(x_train, y_train)
mnb_predict = mnb.predict(x_test)
for i in range(10):
    print(f"actual:{y_test[i]},predict:{mnb_predict[i]}")
    mnb_score = mnb.score(x_test, y_test)
print(f"accuracy(MultinomialNB):{mnb_score}")


print("-------------------")


"""伯努利贝叶斯分类器：BernoulliNB"""
bnb = BernoulliNB().fit(x_train, y_train)
bnb_predict = bnb.predict(x_test)
for i in range(10):
    print(f"actual:{y_test[i]},predict:{bnb_predict[i]}")
bnb_score = bnb.score(x_test, y_test)
print(f"accuracy(BernoulliNB):{bnb_score}")


dic = {"GaussianNB":gnb_score, "MultinomialNB":mnb_score,\
   "BernoulliNB":bnb_score}
#将字典按值排序，即将精确度由大到小排列
lst = sorted(dic.items(), key = lambda x:x[1], reverse = True)
print("-------------------\n精确度由大到小排序：")
for i in lst:
    print(f'{i[0]}   {i[1]}')