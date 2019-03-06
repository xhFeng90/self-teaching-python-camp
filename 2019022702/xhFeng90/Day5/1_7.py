
zen = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#1 将上面的示例字符串 zen 里 better 全部替换成 worse
zen1 = zen.replace('better','worse')
print(zen1)

#2 将上面的示例字符串 zen 里的 大写字母转成小写，小写字母转成大写
zen2 = zen.swapcase()
print(zen2)

#3 将上面的示例字符串 zen 里的包含 ‘ea’ 的英文单词剔除
zen_n = zen.split()
i = 0
l3 = list()

while  i < len(zen_n):
    s = zen_n[i]
    if 'ea' in s:
        l3.append(i)    
    i += 1

for m in sorted(l3,reverse = True):
    del zen_n[m]

zen3 = ' '.join(zen_n)

print(zen3)

#4 将上面的示例字符串 zen 里英文单词 按 a...z 升序排列
zen_new = zen.replace(',','').replace('.','').replace('*','').replace('-','').replace('!','')

zen4 = ' '.join(sorted(zen_new.split()))
print(zen4)


#5 使用列表(list)统计上面的示例字符串 zen 里各个英文单词出现的次数
zen5 = zen4.lower()
l5 = list(sorted(zen5.split()))
set5 = set(l5)
for item in set5:
    if item == 'better':
        print(f'{item} 出现的次数:{l5.count(item)}')

#6 使用字典(dict)统计上面的示例字符串 zen 里各个英文单词出现的次数
d6 = {}
for i in l5:
    if l5.count(i) > 0:
        d6[i] = l5.count(i)
s6 = 'better'
print(f'better 出现的次数:{d6.get(s6)}')

#7 使用集合(set) 统计上面的示例字符串 zen 里出现的英文单词的个数
print(f'英文单词的总个数为：{len(set5)}')







