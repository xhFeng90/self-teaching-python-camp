# 使用 while 循环统计 100 以内能被 7 整除的数的个数，并打印出来
n = 0
x = 1
while x < 100:
    if x%7==0:
        n = n+1
    x = x+1
print(n)