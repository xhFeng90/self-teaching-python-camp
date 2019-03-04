#使用 while 循环判断输入的数字是奇数还是偶数并打印出来，当输入的数字是 0 时则退出循环
x = int(input('请输入数字：'))
while x != 0:
    if x%2 ==0:
        print(x,'是偶数')
    else:
        print(x,'是奇数')
    
    x = int(input('请输入数字：'))

print('程序已终止')