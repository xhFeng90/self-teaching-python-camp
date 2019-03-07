#这是一个斐波那契函数
def fib(n):
    a,b = 0,1
    while a < n:
        print(b,end = ' ')
        a,b = b,a+b
    
    print()