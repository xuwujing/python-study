# List
# 注意：
# 1、List写在方括号之间，元素用逗号隔开。
# 2、和字符串一样，list可以被索引和切片。
# 3、List可以使用+操作符进行拼接。
# 4、List中的元素是可以改变的。


list1 = ['abcd', 123, 2.23, False]
list2 = [234, '1a2B']
# 输出完整列表
print (list1)
# 输出列表第一个元素
print (list1[0])
# 从第二个开始输出到第三个元素
print (list1[1:3])
# 输出从第三个元素开始的所有元素
print (list1[2:])
# 输出两次列表
print (list2 * 2)
# 连接列表
print (list1 + list2)

a = [1, 2, 3, 4, 5, 6]
a[0] = 9
# 将2到5(不包括5)的索引位置值进行替换
a[2:5] = [13, 14, 15]
print(a)
# 将对应的元素值设置为 []
a[2:5] = []
print(a)

# 输出结果
# [9, 2, 13, 14, 15, 6]
# [9, 2, 6]



# 字符串单词反转
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputWords)
    return output


if __name__ == "__main__":
    input = 'Good Good Study'
    rw = reverseWords(input)
    print(rw)


