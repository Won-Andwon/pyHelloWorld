__metaclass__ = type


class Person:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm %s." % self.name)


class Class:
    def method(self):
        print('I have a self!')


class Bird:
    song = 'Squaawk!'

    def __init__(self):
         self.hungry = True

    def sing(self):
         print(self.song)

    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


class Secretive:

    def __inaccessible(self):
        print("Bet you can't see me...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


class C:
    print('Class C being defined...')


class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1


class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is', self.value)


class TalkingCalculator(Calculator, Talker):
    pass


class SomeCustomException(Exception):
    pass


class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise


class FooBar:
    def __init__(self):
        self.somevar = 24

    def __init__(self, value=42):
        self.somevar = value


class A:
    def hello(self):
        print("Hello, I'm A.")


class B(A):
    def hello(self):
        print("Hello, I'm B.")


def checkIndex(key):
    """
    key 应当被接受 即为非负整数
    :param key: 若不是整数 TyperError ;若为负数， IndexError (下面的实现里 希望序列无限长)
    :return:
    """
    if not isinstance(key, int): raise TypeError
    if key<0: raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        初始化算数序列
        :param start: 起始值 序列中的第一个值
        :param step:  步长 两个相邻值
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence.
        :param key:
        :return:
        """
        checkIndex(key)

        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        """
        修改一个项
        :param key:
        :param value:
        :return:
        """
        checkIndex(key)
        self.changed[key] = value


class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = size
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError
    # def __getattribute__(self, item):
    #     pass
    # def __delattr__(self, item):
    #     pass


class OddClass:

    def smeth():
        print('This is a static method')
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print('This is a class method of', cls)
    cmeth = classmethod(cmeth)


class OddClass2:

    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a

    def __iter__(self):
        return self


class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self


def test():
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

if __name__ == '__main__': test()
