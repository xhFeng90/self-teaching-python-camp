#8 将数组 [1,2,3,4,5,6,7,8,9] 翻转，连接，最后输出 int 类型结果: 98764321
l8 = [1,2,3,4,5,6,7,8,9]

l8.remove(5) 

print(''.join(str(i) for i in list(reversed(l8))))