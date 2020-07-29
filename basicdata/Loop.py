# 循环语句 while 和 for 的基本语法

# while 用法
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))


# 死循环
# var = 1
# # 表达式永远为 true
# while var == 1:
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
#
# print("Good bye!")


# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
print("斐波纳契数列结束")




# for循环
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# range 在范围内循环
for i in range(3):
    print(i,end=",")
print("完成range(3)!")

for i in range(3,6):
    print(i,end=",")
print("完成range(3,6)!")

for i in range(2,6,4):
    print(i,end=",")
print("完成range(2,6,4)!")

# len获取索引遍历
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
print(len(a))
for i in range(len(a)):
    print(i, a[i])

# range()函数来创建一个列表
b=list(range(5))
print(b)


