# 元类创建了所有的类型对象（包括object对象），系统默认的元类是type。
# 执行顺序：先定义metaclass，然后在类定义时，通过metaclass创建类，最后通过定义好的类创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，可以把类看成是metaclass创建出来的“实例”。
# 元类中定义的__new__方法，在以该类为元类的类定义时自动调用。例如：类A以类B为元类，当定义类A时，类B的__new__方法将会被自动调用。
# 元类中定义的__call__方法，在以该类为元类的类创建实例时自动调用。例如：类A以类B为元类，当类A创建实例时，类B的__call__方法将会被自动调用。
class MetaClass(type):
    def __init__(cls, *args, **kwargs):
        # cls 代指以该类为元类的类 Foo
        super(MetaClass, cls).__init__(*args, **kwargs)

    def __new__(mcs, *args, **kwargs):
        # mcs 代指元类自身
        print("MetaClass.__new__: ", mcs)
        return super().__new__(mcs, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        # cls 代指以该类为元类的类 Foo
        print("CLS: ", cls)
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)
        return obj


class Foo(metaclass=MetaClass):
    # 定义类Foo时，将调用元类的__new__方法和__init__方法。就跟一般普通类实例化时调用__new__方法和__init__方法一样。
    def __init__(self, name):
        self.name = name


# Foo 实例化时会调用元类的__call__方法。
a = Foo("ABC")