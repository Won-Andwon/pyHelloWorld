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

website = 'http://www.python.org'
# website[-3:] = 'com' TypeError
# 字符串不支持赋值 不可变！

# 字符串格式化 %s
# % d i o u x X e E f F g G C r s
format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values)
format = "Pi with three decimals: %.3f"
from math import pi
print(format % pi)

from string import Template
s = Template('$x, glorious $x!')
print(s.substitute(x='slurm'))
s = Template("It's ${x}tastic!")
print(s.substitute(x='slurm'))
s = Template("Make $$ selling $x!")
print(s.substitute(x='slurm'))
s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print(s.substitute(d))
# safe_substitute

print('%s plus %s equals %s' % (1, 1, 2))
# % (-,+, ,0)转换标志 最小字段宽度(*) .精度/最大字段宽度(*) 转换类型

print('Price of eggs: $%d' % 42)
print('Hexadecimal price of eggs: %x' % 42)
print('Pi: %f...' % pi)
print('Very inexact estimate of pi: %i' % pi)
print('Using str: %s' % 42)
print('Using repr: %r' % 42)
print('%10f' % pi)
print('%10.2f' % pi)
print('%.2f' % pi)
print('%.5s' % 'Guido van Rossum')
# * 从参数读取
print('%.*s' % (5, 'Guido van Rossum'))
print('%010.2f' % pi)
# 左对齐
print('%-10.2f' % pi)
print(('% 5d' % 10) + '\n' + ('% 5d' % -10))
print(('%+5d' % 10) + '\n' + ('%+5d' % -10))

width = input('Please enter width: ')
price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'
print('=' * width)
print(header_format % (item_width, 'Item', price_width, 'Price'))
print('-' * width)
print(format % (item_width, 'Apples', price_width, 0.4))
print(format % (item_width, 'Pears', price_width, 0.5))
print(format % (item_width, 'Cantaloupes', price_width, 1.92))
print(format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8))
print(format % (item_width, 'Prunes (4 lbs.)', price_width, 12))
print('=' * width)

print('With a moo-moo here, and a moo-moo there'.find('moo'))
title = "Monty Python's Flying Circus"
print(title.find('Monty'))
print(title.find('Python'))
print(title.find('Flying'))
print(title.find('Zirquss'))
subject = '$$$ Get rich now!!! $$$'
print(subject.find('$$$'))
print(subject.find('$$$', 1))
print(subject.find('!!!'))
print(subject.find('!!!', 0, 16))
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))
dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs))
print('C:' + '\\'.join(dirs))
print('Trondheim Hammer Dance'.lower())
name = 'Gumby'
names = ['gumby', 'smith', 'jones']
if name.lower() in names:
    print('Found it!')
print("that's all folks".title())
import string
print(string.capwords("that's all folks"))
print('This is a test'.replace('is', 'eez'))
print('1+2+3+4+5'.split('+'))
print('/usr/bin/env'.split('/'))
print('Using the default'.split())
print('   internal whitespace is kept         '.strip())
name = 'gumby '
if name.strip() in names:
    print('Found it!')
print('*** SPAM * for * everyone!!! ***'.strip(' *!'))

table = str.maketrans('cs', 'kz')
print('this is an incredible test'.translate(table))
# 非英语字符串的处理

phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)
print(d['name'])
d = dict(name='Gumby', age=42)
print(d)

x = {}
x[42] = 'Foobar'
print(x)

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')
request = input('Phone number (p) or address (a)?')
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
if name in people:
    print("%s's %s is %s." % (name, labels[key], people[name][key]))

print("Cecil's phone number is %(Cecil)s." % phonebook)
template = """<html>
<head><title>%(title)s</title></head>
<body>
<hl>%(title)s</hl>
<p>%(text)s</p>
</body>"""
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print(template % data)

d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)
returned_value = d.clear()
print(d)
print(returned_value)

# 浅复制 替换值不受影响 修改值原字典会随着变
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)

from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

print({}.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age'], 'unknown'))
d = {}
print(d.get('name'))
print(d.get('name', 'N/A'))

name = input('Name: ')
request = input('Phone number (p) or address (a)? ')
key = request
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("%s's %s is %s." % (name, label, result))

# 3.0后没有 has_key

# Lists as mutable snapshots:
#   d.items() -> list(d.items())
# Iterator objects:
#   d.iteritems() -> iter(d.items())
# Set based dynamic views:
#   d.viewitems() -> d.items()
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(list(d.items()))
# 找不到iteritems
it = iter(d.items())
print(it)
print(list(it))

# 没有 iterkeys
# 改变
# d.keys() -> list(d.keys())
# d.values() -> list(d.values())
# d.items() -> list(d.items())
# d.iterkeys() -> iter(d.keys())
# d.itervalues() -> iter(d.values())
# d.iteritems() -> iter(d.items())
# d.viewkeys() -> d.keys()
# d.viewvalues() -> d.values()
# d.viewitems() -> d.items()

# d.keys() -> list(d)
# d.values() -> list(itervalues(d))
# d.items() -> list(iteritems(d))
# d.iterkeys() -> iter(d)
# d.itervalues() -> itervalues(d)
# d.iteritems() -> iteritems(d)
#
# d.values() -> listvalues(d)
# d.items() -> listitems(d)
#
# d.keys() -> list(d)
# d.values() -> listvalues(d)
# d.items() -> listitems(d)
# d.iterkeys() -> iter(d)
# d.itervalues() -> itervalues(d)
# d.iteritems() -> iteritems(d)
#
# d.keys() -> list(d)
# d.values() -> list(d.values())
# d.items() -> list(d.items())
# d.iterkeys() -> iter(d)
# d.itervalues() -> iter(d.values())
# d.iteritems() -> iter(d.items())

d = {'x': 1,'y': 2}
print(d.pop('x'))
print(d)

d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.popitem())
print(d)

d = {}
d.setdefault('name', 'N/A')
print(d)
d['name'] = 'Gumby'
print(d.setdefault('name', 'N/A'))
print(d)
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2008'
}
x = {'title': 'Python Language Website'}
d.update(x)
print(d)

# logging 模块更适合用于记录日志

print('Age: ', 24)
print(1, 2, 3)
print((1, 2, 3))
name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello,'
print(greeting, salutation, name)
greeting = 'Hello'
print(greeting, ',', salutation, name)
print(greeting + ',', salutation, name)
print('Hello'),
print('world!')
import math as foobar
foobar.sqrt(4)
from math import sqrt as foobar
foobar(4)

# 解包
x, y, z = 1, 2, 3
print(x, y, z)
x, y = y, z
print(x, y, z)
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print(key),
print(value)
# 解包 新
a, b, *rest = [1, 2, 3, 4]

x = y = people.get('mlh')
#等价于
y = people.get('mlh')
x = y

x = 2
x += 1
x *= 2
print(x)
fnord = 'foo'
fnord += 'bar'
fnord *= 2
print(fnord)

# 假 False None 0 "" () [] {}
print(True)
print(False)
print(True == 1)
print(False == 0)
print(True + False + 24)

print(bool('I think, therefore I am'))
print(bool(24))
print(bool(''))
print(bool(0))


name = input("What is your name? ")
if name.endwith('CYC'):
    print('Hello, Mr. CYC')
else:
    print('Hello, stranger')

num = int(input('Enter a number: '))
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')

name = input("What is your name? ")
if name.endwith('CYC'):
    if name.startswith('Mr.'):
        print('Hello, Mr. CYC')
    elif name.startswith('Mrs.'):
        print('Hello, Mrs. CYC')
    else:
        print('Hello, CYC')
else:
    print('Hello stranger')

# x == y
# x < y
# x > y
# x >= y
# x <= y
# x != y
# x is y 同一性而非相等性
# x is not y
# x in y
# x not in y

print("alpha" < "beta")
print("FnOrD".lower() == "Fnord".lower())
print([1, 2] < [2, 1])
print([2, [1, 4]] < [2, [1, 5]])

number = input('Enter a number between 1 and 10: ')
if number <= 10 and number >= 1:
    print('Great!')
else:
    print('Wrong!')
# and or not
# 短路
name = input('Please enter your name: ') or '<unknown>'
print(name)
# a if b else c
age = 10
assert 0 < age < 100
# age = -1
# assert 0< age < 100, 'The age must be realistic'

x = 1
while x <= 100:
    print(x)
    x += 1
name = ''
while not name.strip():
    name = input('Please enter your name: ')
print('Hello, %s!' % name)

words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number)

print(range(0, 10))
print(range(10))
for number in range(1, 51):
    print(number)

d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])
for key, value in d.items():
    print(key, 'corresponds to', value)

names = ['anna', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')
print(zip(names, ages))
for name, age in zip(names, ages):
    print(names[i], 'is', ages[i], 'years old')
print(zip(range(5), range(3455)))
# 只出5个 最短者

strings = ['asdfa', 'adfa', 'dsfsdf', 'sdfa']
for index, string in enumerate(strings):
    if 'fa' in string:
        string[index] = '[censored]'

print(sorted([4, 3, 6, 8, 3]))
print(sorted('Hello, world!'))
print(list(reversed('Hello,world!')))
print(''.join(reversed('Hello, world!')))

for n in range(99, 0 , -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

# for x in seq:
#     if condition1: continue
#     if condition2: continue
#     if condition3: continue
#     do_something()
#     do_something_else()
#     do_another_thing()
#     etc()
# for x in seq:
#     if not (condition1 or condition2 or condition3)
#       do_something()
#       do_something_else()
#       do_another_thing()
#       etc()
while True:
    word = input('Please enter a word: ')
    if not word: break
    print('有病吧，让你干嘛你干嘛！你的输入单词：' + word)
# 循环 的 else(没有因break跳出时调用)
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it!")

# scala yield
print([x*x for x in range(10)])
print([x*x for x in range(10) if x % 3 == 0])
print([(x, y) for x in range(3) for y in range(3)])
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b+'+'+g for b in boys for g in girls if b[0] == g[0]])
# 高效版
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

# pass
if name == 'Ralph Auldus Melish':
    print('Welcome!')
elif name == 'Enid':
    # 不能空语句
    pass
elif name == 'Bill Gates':
    print('Access Denied')

scoundrel = {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
robin = scoundrel
print(scoundrel)
print(robin)
scoundrel = None
print(robin)
# 如果 robin = None 则原来那个字典就漂在内存中， 解释器会自动删除这个字典 即为垃圾收集
# 只能删除名称 不能删除值 解释器负责回收
x = ["Hello", "world"]
y = x
y[1] = "Python"
del x
print(y)
# 依然存在

# 黑暗魔法 创造语句
# 潜在地安全漏洞
# 执行 exec
exec("print('Hello, world')")
from math import sqrt
#exec("sqrt = 1")
#sqrt(4) 报错
scope = {}
exec('sqrt = 1') in scope
print(sqrt(4))
print(scope['sqrt'])

print(len(scope))
print(scope.keys())
#  内建 __builtins__

# eval 求值
print(
    eval(
        input("Enter an arithmetic expression: ")
    )
)
# eval 有命名空间
scope = {}
scope['x'] = 2
scope['y'] = 3
print(eval('x * y', scope))
exec('x = 2' in scope)
print(eval('x*x', scope))
# chr(n)
# ord(c)

# callable() 判断是否可调用
x = 1
y = math.sqrt
print(callable(x))
print(callable(y))
print(hasattr(x, '__call__'))
print(hasattr(y, '__call__'))


def hello(name_in):
    return 'Hello, ' + name_in + '!'


def fibs(num_in):
    res = [0, 1]
    for i in range(num_in - 2):
        res.append(res[-2] + res[-1])
    return res

print(fibs(10))
print(fibs(15))


def square(aNum):
    'Calculates the square of the number aNum.'
    return aNum * aNum
print(square.__doc__)
#print(help(square))


def test():
    print('This is printed')
    return
#    print('This is not')


def change(list_n):
    list_n[0] = 'Mr. CYC'

names = ['Mrs. Entity', 'Mrs. Thing']
change(names)
print(names)
names = ['Mrs. Entity', 'Mrs. Thing']
change(names[:])
print(names)


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

storage = {}
init(storage)
print(storage)


def lookup(data, label, name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
print(lookup(MyNames, 'middle', 'Lie'))

store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
print(lookup(MyNames, 'first', 'Robin'))
store(MyNames, 'Mr. Gumby')
lookup(MyNames, 'middle', '')


def hello_3(greeting='Hello', name='world'):
    print('%s, %s!' % (greeting, name))

hello_3()
hello_3('Greetings')
hello_3('Greetings', 'universe')
hello_3(name='CYC')


def hello_4(name, greeting='Hello', punctuation='!'):
    print('%s, %s%s' % (greeting, name, punctuation))

# 收集至元组中


def print_params(*params):
    print(params)


def print_params_2(title, *params):
    print(title)
    print(params)


print_params_2('Nothing: ')


def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)
print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
print_params_4(1, 2)


def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]
d = {}
init(d)
store(d, 'Han Solo')
store(d, 'Luke Skywalker', 'Anakin Skywalker')
print(lookup(d, 'last', 'Skywalker'))


def add(x, y): return x + y
params = (1, 2)
print(add(*params))
params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)


def foo(x , y, z, m=0, n=0):
    print(x, y, z, m, n)


def call_foo(*args, **kwds):
    print("Calling foo!")
    foo(*args, **kwds)


def story(**kwds):
    return 'Once upon a time, there was a ' \
           '%(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print(story(job='king', name='Gumby'))
print(story(name='Sir Robin', job='brave knight'))
params = {'job': 'language', 'name': 'Python'}
print(story(**params))
del params['job']
print(story(job='stroke of genius', **params))
print(power(2, 3))
print(power(3, 2))
print(power(y=3, x=2))
params = (5,) * 2
print(power(*params))
print(power(3, 3, 'Hello, world'))
print(interval(10))
print(interval(1, 5))
print(interval(3, 12, 4))
print(power(*interval(3, 7)))

x = 1
scope = vars()
print(scope['x'])
scope['x'] += 1
print(x)


def foo():
    x = 42
x = 1
foo()
print(x)


def output(x):
    print(x)
x = 1
y = 2
output(y)


def combine(parameter):
    print(parameter + globals()['patameter'])
parameter = 'berry'
print(combine('Shrub'))

x = 1


def change_global():
    global x
    x = x + 1
change_global(x)
print(x)


def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor
double = multiplier(2)
print(double(5))
triple = multiplier(3)
print(triple(3))
print(multiplier(5)(4))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def power(x, n): # 递归实现
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(search(seq, 34))
print(search(seq, 100))
# 标准库 bisect 二分查找

import functools
# map filter 在 builtin里 (函数)
print(map(str, range(10)))


def func(x):
    return x.isalnum()
seq = ['foo', 'x41', '?!', '***']
print(filter(func, seq))
print([x for x in seq if x.isalnum()])
print(filter(lambda x: x.isalnum, seq))
numbers = [243, 324, 4, 57, 57, 567,54, 32, 674, 674, 54, 63, 56, 74, 345, 25, 674, 67, 45, 54, 80]
print(functools.reduce(lambda x,y: x+y, numbers))
# apply(func[, args[, kwargs]])


# 7.1 多态
print('abc'.count('a'))
print([1, 2, 'a'].count('a'))
from random import choice
x = choice(['Hello world!', [1, 2, 'e', 'e', 4]])
print(x.count('e'))
print(1+2)
print('Fish'+'license')


from study_class import Person
foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()
print(foo.name)
bar.name = 'Yoda'
bar.greet()
Person.greet(foo)

from study_class import Class


def function():
    print("I don't have self")
instance = Class()
instance.method()
# 重新绑定方法（特性？）
instance.method = function
instance.method()

from study_class import Bird
bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()

from study_class import Secretive
s = Secretive()
# s.__inaccessible()
s.accessible()
# s._Secretive__inaccessible()

from study_class import MemberCounter
m1 = MemberCounter()
m1.init()
print(MemberCounter.members)
m2 = MemberCounter()
m2.init()
print(MemberCounter.members)
print(m1.members)
print(m2.members)
m1.members = 'Two'
print(m1.members)
print(m2.members)

from study_class import *
f = Filter()
f.init()
print(f.filter([1, 2, 3]))
s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))
print(issubclass(SPAMFilter, Filter))
print(issubclass(Filter, SPAMFilter))
print(SPAMFilter.__bases__)
print(Filter.__bases__)
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter))
print(isinstance(s, str))
print(s.__class__)
print(type(s))

tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()

print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))
print(callable(getattr(tc, 'talk', None)))
print(callable(getattr(tc, 'fnord', None)))
print(hasattr(getattr(tc, 'fnord', None), '__call__'))
# hasattr(x, '__call__') 代替 callable
setattr(tc, 'name', 'Mr. CYC')
print(tc.name)

print(tc.__dict__)
# inspect 模块 高级

# 8 异常
# Exception
# AttributeError
# IOError
# IndexError
# KeyError
# NameError
# SyntaxError
# TypeError
# ValueError
# ZeroDivisionError

try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x/y)
except ZeroDivisionError:
    print("The second number can't be zero!")
except TypeError:
    print("That wasn't a number, was it?")
except (NameError, ValueError, SyntaxError) as e:
    print('Your numbers were bogus...')
    print(e)
except: #相当危险 甚至捕捉Ctrl+C操作 sys.exit等
    print('Something wrong happened...')

calculator = MuffledCalculator()
calculator.calc('10/2')
# calculator.calc('10/0')
calculator.muffled = True
calculator.calc('10/2')


try:
    print('A simple task')
except Exception as e:
    print('What? Something went wrong?')
    print(e)
else:
    print('Ah... It went as planned.')

while True:
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        value = x / y
        print('x/y is ', value)
    except Exception as e:
        print('Invalid input: %s\nPlease try again.' % e)
    else:
        break

try:
    1/0
except NameError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("Cleaning up.")


def faulty():
    raise Exception('Something is wrong')


def ignore_exception():
    faulty()


def handle_exception():
    try:
        faulty()
    except:
        print('Exception handled')

# ignore_exception()
handle_exception()

# try/catch 能更高效 更自然易读


def describePerson(person):
    print('Description of ', person['name'])
    print("Age: ", person['age'])
    try:
        print('Occupation: ' + person['occupation'])
    except KeyError:
        pass
# 只需要根据键值获取一次，如果用if 则判定了有这个键值 还需要再获取一次，try的话 没有就走报错了
try:
    tc.write
except AttributeError:
    print('The object is not writeable')
else:
    print('The object is writeable')

# import warnings
# warnings.filterwarnings()

# __init__ 尝试
f = FooBar()
print(f.somevar)
f = FooBar('This is a constructor argument')
print(f.somevar)
sb = SongBird()
sb.sing()
sb.eat()
sb.eat()


s = ArithmeticSequence(1, 2)
print(s[4])
s[4] = 2
print(s[4])
print(s[5])

c1 = CounterList(range(10))
print(c1)
c1.reverse()
print(c1)
del c1[3:6]
print(c1)
print(c1.counter)
print(c1[4] + c1[2])
print(c1.counter)

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

ti = TestIterator()
print(list(ti))


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print(num)
print(list[1, 2, 3, 4, 5])

g = ((i+2)**2 for i in range(2, 27))
print(next(g))
print(sum(i**2 for i in range(10)))

# 小技巧：检查是否是字符串， 将传入与一个字符串拼接，看是否出现TypeError


def flatten_2(nested):
    try:
        # 不迭代类似字符串的对象：
        try: nested + ' '
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

print(list(flatten_2(['foo', ['bar', ['baz']]])))


def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

r = repeater(42)
print(next(r))
print(r.send("Hello, world!"))
# thorw close


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            # X取值差 既不等同（0），也不等同Y取值差
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos, )
            else:
                for result in queens(num, state + (pos, )):
                    yield (pos, ) + result
print(list(queens(3)))
print(list(queens(4)))
print(len(list(queens(8))))


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))
import random
prettyprint(random.choice(list(queens(8))))

import sys, pprint
pprint.pprint(sys.path)

# 10.3 标准库
import sys
# argv
# exit([arg])
# modules
# path
# platform
# stdin
# stdout
# stderr
args = sys.argv[1:]
args.reverse()
print(' '.join(args))
print(' '.join(reversed(sys.argv[1:])))

import os
# path模块 检查 构造 删除 目录或文件 处理路径等
# os.environ
# os.system(command=)
# os.sep
# os.pathsep
# os.linesep
# os.urandom(n)

# os.system('/usr/bin/firefox')
# os.system(r'c:\"Program Files"\"Mozilla Firefox"\firefox.exe')
# os.startfile(r'c:\Program Files\Mozilla Firefox\firefox.exe')
# import webbrowser
# webbrowser.open('htt://www.python.org')

import fileinput
# fileinput.input()
# fileinput.filename()
# fileinput.lineno()
# fileinput.filelineno()
# fileinput.isfirstline()
# fileinput.isstdin()
# fileinput.nextfile()
# fileinput.close()
# for line in fileinput.input(inplace=True):
#     line = line.rstrip()
#     num = fileinput.lineno()
#     print('%-40s # %2i' % (line, num))

print(set(range(10)))
print(set([0, 1, 2, 3, 0, 1, 2, 3, 4, 5]))
print(set(['fee', 'fie', 'foe']))
a = set([1, 2, 3])
b = set([4, 2, 3])
print(a.union(b))
print(a | b)
c = a & b
print(c.issubset(a))
print(c <= a)
print(c.issuperset(a))
print(c >= a)
print(a.intersection(b))
print(a & b)
print(a.difference(b))
print(a - b)
print(a.symmetric_difference(b))
print(a ^ b)
print(a.copy())
print(a.copy() is a)
# add remove
mySets = []
for i in range(10):
    mySets.append(set(range(i, i+5)))
import functools
print(functools.reduce(set.union(), mySets))
a = set()
b = set()
a.add(frozenset(b))

import heapq
# 堆
# heapq.heappush()
# heapq.heappop()
# heapq.heapify()
# heapq.heapreplace()
# heapq.nlargest()
# heapq.nsmallest()
from random import shuffle
data = range(10)
shuffle(data)
heap = []
for n in data:
    heapq.heappush(heap, n)
print(heap)
heapq.heappush(heap, 0.5)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)
heap = [5, 8, 0 , 3, 6, 7, 9, 1, 4, 2]
heapq.heapify(heap)
print(heap)
# heapreplace < heappop+heappush
print(heapq.heapreplace(heap, 0.5))
print(heap)
print(heapq.heapreplace(heap, 10))
print(heap)

from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
print(q.pop())
print(q.popleft())
q.rotate(3)
print(q)
q.rotate(-1)
print(q)

import time
# (2008, 1, 21, 12, 2, 56, 0 , 21, 0) 2008年1月21日12时2分56秒 星期一 当年第21天 无夏令时
# time.asctime([tuple]) 时间元组转换为字符串
# time.localtime([secs]) 秒数转换为元组
# time.mktime(tuple) 元组转换为本地时间
# time.sleep(secs) 休眠
# time.strptime(string[, format]) 字符串解析成元组
# time.time()  当前时间 秒数
print(time.asctime())
# datetime timeit(计时)模块

import random
# random.random() 0~1
# random.getrandbits(n) 给定位数 二级制 长整形值
# random.uniform(a, b) a~b间随机实数
# random.randrange([start, ]stop[, stop]) 返回range中的随机数
# random.choice(seq) 随机抽取一个
# random.shuffle(seq[, random]) 打乱
# random.(seq, n) 随机采样
date1 = (2008, 1, 1, 0, 0 , 0, -1, -1 ,-1)
time1 = time.mktime(date1)
date2 = (2009, 1, 1, 0, 0 , 0, -1, -1 ,-1)
time2 = time.mktime(date2)
random_time = random.uniform(time1, time2)
print(time.asctime(time.localtime(random_time)))
from random import randrange
num = input('How many dice? ')
sides = input('How many sides per dice? ')
sum = 0
for i in range(num):
    sum += randrange(sides) + 1
print('The result is', sum)

values = range(1, 11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v ,s) for v in values for s in suits] + ['black jocker', 'red jocker']
shuffle(deck)
# while deck:
#     input(deck.pop())

import shelve
# s = shelve.open('test.dat')
# s['x'] = ['a', 'b', 'c']
# s['x'].append('d')
# print(s['x'])
# # 并未改变
# temp = s['x']
# temp.append('d')
# s['x'] = temp
# print(s['x'])
# # 真正改变
# 参见 code10-8

import re
# 正则
# .
# \\. 解释器转义 正则转义
# [py] [a-z] [^abc]
# python | perl p(ython|erl)
# ? r'(http://)?(www\.)?python\.org'
# (pattern)* 0以上
# (pattern)+ 1以上
# (pattern){m, n} m~n
# ^ $

# re.compile(pattern[, flags])
# re.search(pattern=, string=[, flags])
# re.match(pattern=, string=[, flags])
# re.split(pattern=, string=[, maxsplit=0])
# re.findall(pattern=, string=)
# re.sub(pat, repl, string[, count=0])
# re.escape(string)

some_text = 'alpha, beta,,,,gamma  delta'
print(re.split('[, ]+', some_text))
pat = '[a-zA-Z]+'
text = '"hm... Err -- are you sure?" he said, sounding insecure.'
print(re.findall(pat, text))
pat = r'[.?\-",]+'
print(re.findall(pat, text))
pat = '{name}'
text = 'Dear {name}...'
re.sub(pat, 'Mr. CYC', text)
print(re.escape('www.python.org'))
print(re.escape('But where is the ambiguity?'))

m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
print(m.group(1))
print(m.start(1))
print(m.end(1))
print(m.span(1))

emphasis_pattern = r'\*([^\*]+)\*'
print(re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!'))

#其他模块
# import functools
# import difflib
# import hashlib
# import csv
# import timeit
# import profile
# import trace
# import datetime
# import itertools
# import logging
# import getopt
# import optparse
# import cmd








