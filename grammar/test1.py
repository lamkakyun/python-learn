#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 使用元类

def fn(self, name="world"):
    print("hello %s" % name )

Hello = type('Hello', (object,), dict(hello=fn)) # 动态创建一个类
h = Hello()
print(h.hello('jet'))
print(type(Hello))
print(type(h))
# 以上是普通的类，的动态创建，之后使用元类

class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs) # 创建类时，将增加add 方法

class MyList(list):
    __metaclass__ = ListMetaClass

l = MyList()
l.add(10)
print(l)