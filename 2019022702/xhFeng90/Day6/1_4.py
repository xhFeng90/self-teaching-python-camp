#定义一个函数，以年份为参数，判断输入的年份是平年还是闰年

def leap_everage(year):
   
    if year % 4 == 0 and year % 100 != 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is an everage year')

leap_everage(int(input('please input the year: ')))



#定义一个函数，以 n 为参数，输出 n 项 斐波那契数列

def fib(n):
    a,b = 0,1
    i = 0
    while  i < n:
        print(b,end=' ')
        a,b = b,a+b
        i += 1

fib(10)

#定义一个函数，以 n 为参数，返回距今 n 天前是星期几

import datetime

def week(n):
    d = datetime.datetime.now()
    p = d.weekday()#不知道为什么调用内置函数，今天是星期几，显示不对。
    l = n % 7
    if l < p:
        print(f'距离今天{n}天前是星期{p-l}')
    elif l == p:
        print(f'距离今天{n}天前是星期天')
    else:
        print(f'距离今天{n}天前是星期{p-l+7}')
    
    print(f'今天是星期{p}')

week(100)


#把 斐波那契 函数定义在一个模块里，在另一个文件里调用斐波那契函数
import fibo
fibo.fib(100)


