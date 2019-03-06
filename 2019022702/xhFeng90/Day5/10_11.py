#10 用字符串切片的方式取出’Hello, World!’ 中第三到第八个字符(包含第三和第八个字符)。

s_new = 'Hello, World!'
s10 = s_new[2:8]
print(s10)

#11 将 'Hello, World!' 进行反转，输出结果 '!dlroW ,olleH'
s11 = list(s_new)
n11 = len(s11)
ls11 = []

while n11 > 0:
    p11 = s11.pop(n11-1)
    ls11.append(p11)
    n11 -= 1

print(''.join(ls11))