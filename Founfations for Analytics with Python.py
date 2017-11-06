from math import exp,log,sqrt
import re
from datetime import date,time,datetime,timedelta
from operator import itemgetter
from numpy as np


#for
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta','Holly', 'Isabel', 'Jenny']

print("Output #129:")
for month in y:                                                       
    
    print("{!s}".format(month))                                       

print("Output #130: (index value: name in list)")
for i in range(len(z)):
    print("{0!s}: {1:s}".format(i, z[i]))

print("Output #131: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'):
        print("{!s}".format(y[j]))

print("Output #132:")
for key, value in another_dict.items():
    print("{0:s}, {1}".format(key, value))
    
    
    
    
    
#for variable in sequence ,variable是一个临时占位符（一个变量名），表示序列中的各个值，sequence是要进行迭代的序列的名称。
#len()函数返回列表中元素的个数，rang()函数生成了一系列整数，是从0开始直到len函数结果少1的整数
#startswith()判断是否以。。。为开头。


#使用列表生成式选择特定的行
my_data = [[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Output #133 (list comprehension): {}".format(rows_to_keep))

#row在这里也是一个临时占位符,同时也是列表返回的值

#使用集合生成式在列表中选择出一组唯一的元组
#使用集合生成式在列表中选择出一组唯一的元组
my_data = [(1,2,3),(4,5,6),(7,8,9),(7,8,9)]
set_of_tuples1 = {x for x in my_data}
print("Output #133(set comprehension):{}".format(set_of_tuples1))
set_of_tuples2 = set(my_data)
print("OUtput #132(set function):{}".format(set_of_tuples2))



#使用字典生成式选择特定的键值对
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
my_results = {key : value for key, value in my_dictionary.items() if value > 10}
print("Output #136 (dictionary comprehension): {}".format(my_results))

#字典返回的值的格式是:key : value


#while循环
print("Output #134:")
x = 0
while x < 11:
    print("{!s}".format(x))
    x+=1
    
#计算一系列数值的均值
def getMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues)>0 else float('nan')
my_list = [2,2,4,4,6,6,8,8]
print("Output #135(mean):{!s}".format(getMean(my_list)))
#if len(numericValues)>0 else float('nan')这句话用来检验是否是个空列表

#使用Numpy中存在的mean函数
#print np.mean(my_list)

#展示两种两种使用try-except代码块来有效捕获和处理异常的方法
def getMean(numericValues):
    return sum(numericValues)/len(numericValues) 
my_list2 =[]
try:
    print("Output #138:{}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print()

#1.5读取文本文件
#导入sys模块  import sys
#读取文件
#读取单个文本文件
#脚本和文本在同一位置
input_file = sys.argv[1]

print("Output #143:")
filereader = open(input_file,'r')
for row in filereader:
    print(row.strip())
filereader.close()
#argv[1]是命令行传递给脚本的第一个参数

#1.5.2脚本和文件不在同一位置
#python first_script.py "文件的地址"

#读取文件的新型语法












































