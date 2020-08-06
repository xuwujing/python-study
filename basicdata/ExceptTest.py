# 错误和异常 异常捕捉可以使用 try/except 语句

while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")

# 请输入一个数字: fff
# 您输入的不是数字，请再次尝试输入！
# 请输入一个数字: 111


# try/except...else

while True:
    try:
        x = int(input("请输入一个数字: "))
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
    else:
        print("您輸入的数字:"+x)
        break