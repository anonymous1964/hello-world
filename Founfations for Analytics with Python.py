#for
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', \
'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', \
'Holly', 'Isabel', 'Jenny']

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
