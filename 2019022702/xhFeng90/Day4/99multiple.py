#打印99乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print(x,'*',y,'=',x*y,sep=' ',end='  ')
    print(' ')
