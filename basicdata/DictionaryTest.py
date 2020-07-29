# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
# 注意：
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。


dict = {}
dict['one'] = "1 - hello"
dict[2]     = "2 - world"
tinydict = {'name': 'pancm','age':18, 'site': 'www.panchengming.com'}
# 输出键为 'one' 的值
print (dict['one'])
# 输出键为 2 的值
print (dict[2])
# 输出完整的字典
print (tinydict)
# 输出所有键
print (tinydict.keys())
# 输出所有值
print (tinydict.values())

