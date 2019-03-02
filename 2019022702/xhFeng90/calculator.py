x,y,z = input("请输入计算式，注意用空格隔开数字和运算符:").split()
x = int(x)
z = int(z)

if y == "+":
    a = x + z
    print('结果是：',a)

elif y == "-":
    a = x - z
    print('结果是：',a)
    
elif y == "*":
    a = x * z
    print('结果是：',a)

elif y == "/":
    a = x/z
    print('结果是：',a)