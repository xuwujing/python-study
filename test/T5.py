# 数据类型，python的数据类型是根据变量值来决定的，和JavaScript类似
# 整数
a = 10
# 浮点
b = 10.5
# 字符串
c = "11"

print(a)
print(b)
print(c)

# 多个变量赋值
d,e,f = 1+2j,True,"2"
print(d)
print(e)
print(f)

# 可以通过type查看类型
print(type(a), type(b), type(c), type(d), type(e))
# 也可以通过isinstance方法判断
print(isinstance(a,int))
print(isinstance(a,str))



# 输出结果
# 10
# 10.5
# 11
# (1+2j)
# True
# 2
# <class 'int'> <class 'float'> <class 'str'> <class 'complex'> <class 'bool'>
# True
# False

