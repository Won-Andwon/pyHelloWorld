import time
import math
from math import sqrt
import cmath
from functools import cmp_to_key

# 1.4 数字和表达式
print(2 + 2)
print(53672 + 235253)

print(1/2)
print(1.0/2.0)
print(1/2.0)
print(1.0/2)
print(1/2)

# from __future__ import division

print(1 // 2)
print(1.0//2.0)

print(1 % 2)
print(10 / 3)
print(10 % 3)
print(9 / 3)
print(9 % 3)
print(2.75 % 0.5)

print(2 ** 3)
print(-3 ** 2)
print((-3) ** 2)

# python3.5以上 不支持l以及L
print(1000000000000000000)
print(398234729752483 * 230982093482093823 + 23)

print(0xAF)
print(0o10)

# 1.5 变量
x = 3
print(x * 2)

# 1.6 语句
print(2 * 2)

# 1.7 获取用户输入（标准输入）

input("The meaning of life: ")
x = int(input("x = "))
y = int(input("y = "))
print(x * y)
# 管窥 if 语句
if 1 == 2:
    print('One equals two')
if 1 == 1:
    print('One equals one')

if time.localtime()[4] % 60 == 0:
    print('On the hour!')

# 1.8 函数
pow(2, 3)
10 + pow(2, 3*5)/3.0
abs(-10)
round(1.0/2.0)

# 1.9 模块

math.floor(32.9)
int(math.floor(32.9))

sqrt(9)

cmath.sqrt(-1)
print((1 + 3j) * (9 + 4j))

# 1.10 保存和执行程序
# 3.1版本后没raw_input了！
name = input("What is your name? ")
print('Hello,' + name + '!')
# python study.py
# #!/usr/bin/env python
# chmod a+x hello.py
input("Press <enter>...")

# 1.11 字符串
"Let's go!"
'"Hello, world!" she said'
'Let\'s go!'
"\"Hello, world!\" she said"
print("Hello, " + "world!")
x = "Hello, "
y = "world!"
print(x + y)

print(repr("Hello, world!"))
# 没有 long()函数了
print(repr(10000))
print(str("Hello, world!"))
print(str(10000))
temp = 42
# 不支持 ``了
print("The temperature is " + repr(temp))
# 没有raw_input了
print("""This is a very long string.
It continues here.
And it's not over yet.
"Hello, world!"
Still here.""")
print("Hello, \
world!")
print(1 + 2 +\
    4 + 5)
print\
    ("Hello, world!")
print("Hello,\nworld!")
path = 'C:\nowhere'
print(path)
print('C:\\nowhere')
print('F:\\Users\\Won Andwon\\PycharmProjects\\pyHelloWorld\\study.py')
# 原始字符串 r''
print(r'C:\nowhere')
print(r'Let\'s go!')
# 末尾加\
print(r'C:\Program Files' '\\')
# unicode字符串
u'Hello, world!'

# 2.1 序列概览
Edward = ['Edward Gumby', 42]
John = ['John Smith', 42]
database = [Edward, John]
print(database)

# 2.2 通用序列操作
greeting = 'Hello'
print(greeting[0])
print(greeting[-1])
print('Hello'[1])
fourth = input('Year: ')[3]
print(fourth)

# 年月日处理
months = [
    'January',
    'February',
    'Match',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] +  7 * ['th'] \
        + ['st']
year  = input('Year: ')
month = input('Month(1-12): ')
day   = input('Day(1-31): ')
month_number = int(month)
day_number = int(day)
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print(month_name + ' ' + ordinal + ', ' + year)

tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
print(tag[32:-4])
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
print(numbers[7:10])
print(numbers[-3:-1]) # 倒数两个
print(numbers[-3:0]) # 空
# 索引置空
print(numbers[-3:])
print(numbers[:3])
print(numbers[:])

domain = 'http://www.python.org'[11:-4]
print("Domain name: " + domain)

print(numbers[::1])
print(numbers[::2])
print(numbers[3:6:3])
print(numbers[8:3:-1])
print(numbers[10:0:-2])
print(numbers[0:10:-2])
print(numbers[::-2])
print(numbers[5::-2])
print(numbers[:5:-2])

print([1, 2, 3] + [4, 5, 6])
print('Hello, ' + 'world!')

print('python' * 5)
print([42] * 10)
sequence = [None] * 10
print(sequence)

sentence = input("Sentence: ")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
print()
print(' ' * left_margin + '+' + '_' * (box_width - 2) + '+')
print(' ' * left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '|' + sentence + '|')
print(' ' * left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '+' + '_' * (box_width - 2) + '+')
print()

permissions = 'rw'
print('w' in permissions)
print('x' in permissions)
users = ['mlh', 'foo', 'bar']
print(input('Enter your user name: ') in users)
subject = '$$$ Get rich now!!! $$$'
print('$$$' in subject) # 检查子串

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]
username = input('User name: ')
pin = input('PIN code: ')
if [username, pin] in database:
    print('Access granted')

numbers = [100, 34, 678]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(max(2, 3))
print(min(9, 3, 2, 5))

# 2.3 列表 list
print(list('Hello'))
print(''.join(list('Hello')))
x = [1, 1, 1]
x[1] = 2
print(x)
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)
name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)
name[1:] = list('ython')
print(name)
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)
numbers[1:4] = []
print(numbers)

lst = [1, 2, 3]
print(lst)
lst.append(4)
print(lst)

print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1))
print(x.count([1, 2]))

a = [1, 2, 3]
b = [4, 5, 6]
# 变a 高效
a.append(b)
print(a)

a[len(a):] = b

knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
knights.index('who')
# 报错 不存在 knights.index('herring')
print(knights[4])

numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)
numbers = [1, 2, 3, 5, 6, 7]
numbers[3:3] = ['four']
print(numbers)

x = [1, 2, 3]
print(x.pop())
print(x)
print(x.pop(0))
print(x)
x = [1, 2, 3]
print(x)
x.append(x.pop())
print(x)

x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print(x)
# 报错 没有 x.remove('bee')
x = [1, 2, 3]
x.reverse()
print(x)
x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)
x = [4, 6, 2, 1, 7, 9]
y = x.sort() # sort return nothing! Don't do this
print(y)

x = [4, 6, 2, 1, 7, 9]
y = x[:] # 此为复制 若 y = x 则相当于两个指向同一list（类似引用）
y.sort()
print(x)
print(y)
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print(x)
print(y)
print(sorted('Python'))

# cmp在3.5里没啦！ 换成 lt le eq ne gt ne
print(cmp_to_key(42, 32))
print(cmp_to_key(99, 100))
print(cmp_to_key(10, 10))
numbers = [5, 2, 9, 7]
numbers.sort(cmp_to_key)
print(numbers)
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print(x)
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)

# 2.4 元祖 不可变序列
print(1, 2, 3)
print((1, 2, 3))
print(())
print(42,)
print((42,))
print(3*(42+2))
print(3*(42+2,))

print(tuple([1, 2, 3]))
print(tuple('abc'))
print(tuple((1, 2, 3)))
x = 1, 2, 3
print(x[1])
print(x[0:2])




















































































