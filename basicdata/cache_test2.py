"""
# 基于磁盘的缓存，会存在本地

教程 https://joblib.readthedocs.io/en/latest/memory.html
安装 pip install joblib
"""

from joblib import Memory

memory = Memory(location="./cachedir")

@memory.cache
def sum2(a,b):
    print(f"计算{a}+{b} ... ")
    return a+b


print(sum2(2,3))
print(sum2(2,3))

print(sum2(4,7))
print(sum2(4,7))


print(sum2(2,3))
print(sum2(4,7))
