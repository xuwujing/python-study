# JSON 转换
# Python
# JSON
# dict
# object
# list, tuple
# array
# str
# string
# int, float, int- & float-derived Enums
# number
# True
# true
# False
# false
# None
# null

import json

# Python 字典类型转换为 JSON 对象
data = {
    'id': 1,
    'name': 'xuwujing',
    'url': 'http://www.panchengming.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)


# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data3 = json.load(f)
    print("读取的data.json文件数据:",data3)

