# 迭代器使用
list=[1,2,3,4]
it = iter(list)
it2 = iter(list)
for i in range(2):
   print (next(it),end=",")
print("结束")
for i in it2:
   print (i,end=",")
print("结束")

#输出:
# 1,2,结束
# 1,2,3,4,结束


# 创建一个迭代器，需要在类中实现两个方法 __iter__() 与 __next__()

class TestIter1:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
         x=self.a
         self.a+=1
         return x

myClass = TestIter1()
myIter = iter(myClass)

for i in range(5):
    print(next(myIter),end=",")
print("自定义迭代器结束！")

# 输出结果
# 1,2,3,4,5,自定义迭代器结束！


# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class TestIter2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a<=8:
            x = self.a
            self.a += 1
            return x
        else:
            raise  StopIteration

myClass2 = TestIter2()
myIter2 = iter(myClass2)
for i in myIter2:
    print(i, end=",")
print("自定义迭代器结束！")

# 输出结果
# 1,2,3,4,5,6,7,8,自定义迭代器结束！

#  yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
# 调用一个生成器函数，返回的是一个迭代器对象。
import sys
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()


