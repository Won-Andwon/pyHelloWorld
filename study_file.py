import pprint

f = open(r'D:\Data\Python_test.txt', 'w')
# 'r' 'w' 'a' 'b' '+'
f.write('Hello, ')
f.write('World!')
f.close()

f = open(r'D:\Data\Python_test.txt')
print(f.read(5))
pprint.pprint(f.read())
f.close()

# import sys
# text = sys.stdin.read()
# words = text.split()
# wordcount = len(words)
# print('Wordcount:', wordcount)

with open(r'D:\Data\Python_test.txt', 'w') as f:
    f.write('01234567890123456789')
    f.seek(5)
    f.write('Hello, World!')

with open(r'D:\Data\Python_test.txt') as f:
    pprint.pprint(f.read())

with open(r'D:\Data\Python_test.txt') as f:
    print(f.read(3))
    print(f.read(2))
    print(f.tell())

with open(r'D:\Data\Python_test.txt') as f:
    print(f.read(7))
    print(f.read(4))

with open(r'D:\Data\Python_test.txt') as f:
    pprint.pprint(f.read())

with open(r'D:\Data\Python_test.txt') as f:
    for i in range(3):
        print(str(i) + ":" + f.readline())

pprint.pprint(open(r'D:\Data\Python_test.txt').readlines())

with open(r'D:\Data\Python_test.txt', 'w') as f:
    f.write('this\nis no\nhaiku')

with open(r'D:\Data\Python_test.txt') as f:
    lines = f.readlines()
lines[1] = "isn't a\n"

with open(r'D:\Data\Python_test.txt', 'w') as f:
    f.writelines(lines)

# f = open(filename)
# while True:
#     char = f.read(1)
#     if not char: break
#     process(char)
# f.close()
#
# f = open(filename)
# while True:
#     line = f.readline()
#     if not line: break
#     process(line)
# f.close()
#
# f = open(filename)
# for char in f.read():
#     process(char)
# f.close()
#
# f = open(filename)
# for line in f.readlines():
#     process(line)
# f.close()
# import fileinput
# for line in fileinput.input(filename):
#     process(line)

# for line in open(filename):
#     process(line)
# import sys
# for line in sys.stdin:
#     process(line)
f = open(r'D:\Data\Python_test.txt', 'w')
f.write('First line\n')
f.write('Second line\n')
f.write('Third line\n')
f.close()
lines = list(open(r'D:\Data\Python_test.txt'))
print(lines)
first, second, third = open(r'D:\Data\Python_test.txt')
print(first)
print(second)
print(third)
f.close()
