# String类型 Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符
# 注意：
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。


a="abcdefg"
# 不换行 end=" "
print( a, end=" " )
# 输出第一个到倒数第二个的所有字符
print(a[0:-1])
# 输出字符串第一个字符
print(a[0])
#输出从第三个开始后的所有字符
print(a[2:])
# 输出字符串两次
print(a*2)
# 字符串相加
print(a+",pancm")

# Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
print('pa\nncm')
print(r'pa\nncm')
# 输出结果
# pa
# ncm
# pa\nncm


# str.format将数据进行格式化，类似java的String.format
print("{}:你好,{}".format("python","hi"))
# python:你好,hi
print("{name}:你好,{word}".format(name="python",word="hi"))
# python:你好,hi

