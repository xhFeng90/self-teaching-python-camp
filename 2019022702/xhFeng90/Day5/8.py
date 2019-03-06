#8 将数组 [1,2,3,4,5,6,7,8,9] 翻转，连接，最后输出 int 类型结果: 98764321
l8 = [1,2,3,4,5,6,7,8,9]
n = len(l8)
ls = []

while n > 0:
    p = l8.pop(n-1)
    ls.append(p)
    n-=1

ls_new = [str(i) for i in ls]
s = ''.join(ls_new)

print(s)