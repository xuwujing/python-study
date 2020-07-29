# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：
# parame = {value01,value02,...}
# 或者
# set(value)

sites = {'Google', 'Taobao',  'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'bibibi' in sites :
    print('bibibi 在集合中')
else :
    print('bibibi 不在集合中')

# set可以进行集合运算
a = set('abcdefg')
b = set('acdfh')

print(a)
# a 和 b 的差集
print(a - b)
# a 和 b 的并集
print(a | b)
# a 和 b 的交集
print(a & b)
# a 和 b 中不同时存在的元素
print(a ^ b)

# 输出结果
# {'Google', 'Facebook', 'Taobao', 'Zhihu', 'Baidu'}
# bibibi 不在集合中
# {'a', 'g', 'e', 'b', 'f', 'd', 'c'}
# {'g', 'b', 'e'}
# {'a', 'b', 'c', 'f', 'h', 'e', 'd', 'g'}
# {'a', 'd', 'f', 'c'}
# {'b', 'g', 'h', 'e'}