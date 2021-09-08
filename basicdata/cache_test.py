from functools import lru_cache


# maxsize=1，表示可以缓存的元素的个数。
# 改变maxsize的值为2，再切换为1，运行程序观察输出结果.
# sum2.cache_info()    #查看缓存性能
# sum2.cache_clear()   #清除缓存

@lru_cache(maxsize=1)
def sum2(a,b):
    print(f"计算{a}+{b} ... ")
    return a+b


print(sum2(2,3))
print(sum2(2,3))

print(sum2(4,7))
print(sum2(4,7))


print(sum2(2,3))
print(sum2(4,7))
