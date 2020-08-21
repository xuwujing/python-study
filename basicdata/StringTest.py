# String类型 Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符
# 注意：
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。
# 1
# capitalize()
# 将字符串的第一个字符转换为大写
#
# 2
# center(width, fillchar)
#
#
# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
# 3
# count(str, beg= 0,end=len(string))
#
#
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
# 4
# bytes.decode(encoding="utf-8", errors="strict")
#
#
# Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
# 5
# encode(encoding='UTF-8',errors='strict')
#
#
# 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
# 6
# endswith(suffix, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
#
# 7
# expandtabs(tabsize=8)
#
#
# 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
# 8
# find(str, beg=0, end=len(string))
#
#
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
# 9
# index(str, beg=0, end=len(string))
#
#
# 跟find()方法一样，只不过如果str不在字符串中会报一个异常。
# 10
# isalnum()
#
#
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
# 11
# isalpha()
#
#
# 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
# 12
# isdigit()
#
#
# 如果字符串只包含数字则返回 True 否则返回 False..
# 13
# islower()
#
#
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
# 14
# isnumeric()
#
#
# 如果字符串中只包含数字字符，则返回 True，否则返回 False
# 15
# isspace()
#
#
# 如果字符串中只包含空白，则返回 True，否则返回 False.
# 16
# istitle()
#
#
# 如果字符串是标题化的(见 title())则返回 True，否则返回 False
# 17
# isupper()
#
#
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# 18
# join(seq)
#
#
# 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# 19
# len(string)
#
#
# 返回字符串长度
# 20
# ljust(width[, fillchar])
#
#
# 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
# 21
# lower()
#
#
# 转换字符串中所有大写字符为小写.
# 22
# lstrip()
#
#
# 截掉字符串左边的空格或指定字符。
# 23
# maketrans()
#
#
# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 24
# max(str)
#
#
# 返回字符串 str 中最大的字母。
# 25
# min(str)
#
#
# 返回字符串 str 中最小的字母。
# 26
# replace(old, new [, max])
#
#
# 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
# 27
# rfind(str, beg=0,end=len(string))
#
#
# 类似于 find()函数，不过是从右边开始查找.
# 28
# rindex( str, beg=0, end=len(string))
#
#
# 类似于 index()，不过是从右边开始.
# 29
# rjust(width,[, fillchar])
#
#
# 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
# 30
# rstrip()
#
#
# 删除字符串字符串末尾的空格.
# 31
# split(str="", num=string.count(str))
#
#
# 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
# 32
# splitlines([keepends])
#
#
# 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
# 33
# startswith(substr, beg=0,end=len(string))
#
#
# 检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
# 34
# strip([chars])
#
#
# 在字符串上执行 lstrip()和 rstrip()
# 35
# swapcase()
#
#
# 将字符串中大写转换为小写，小写转换为大写
# 36
# title()
#
#
# 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
# 37
# translate(table, deletechars="")
#
#
# 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
# 38
# upper()
# 转换字符串中的小写字母为大写
# 39
# zfill (width)
#
#
# 返回长度为 width 的字符串，原字符串右对齐，前面填充0
# 40
# isdecimal()
#
#
# 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。


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
a1='ww'
a2=1
a3 = a1+','+str(a2)
print(a3)

b=(14942, 11, 'HK_DXH_020100000001132734ea0003e92', '52063c31cf6c3e9a17ba9ff56f5135ec', 'e8611f2b031f', '', '27.11.2.5', 'slot=2;subslot=0;port=10;vlanid=113', 'Ethernet', '2020-08-05 20:18:27', '2020-08-05 20:18:27', None, 0, None, 'RADIUS', '', '', 0, 0, '80-D4-A5-08-49-70', 'e861-1f2b-031f', '', 'Framed-User', 'PPP', '27.23.18.55', '', '', '', '', '2020-08-05 20:18:27')

print(str(b).replace('(','').replace(')',''))

