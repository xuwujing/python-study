# python时间格式获取和转换

import time
import calendar

ticks = time.time()
print ("当前时间戳为:", ticks)

print ("当前时间戳为格式化:", int(time.time()))

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)


timeArray = time.localtime(ticks)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print("本地时间格式化:",otherStyleTime)
# python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身


# 格式化成yyyy-MM-dd hh:mm:ss形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


# 获取日历
cal = calendar.month(2020, 8)
print ("以下输出2020年8月份的日历:")
print (cal)

# 字符类型的时间1
tss1 = '2019-05-31 15:12:54'
# 转为时间数组
timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
print(timeArray)
# 转为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)  # 1559286774
print(int(time.mktime(time.strptime(tss1, "%Y-%m-%d %H:%M:%S"))))
# timeArray可以调用tm_year等
print(timeArray.tm_year)   # 2019
# 字符类型的时间2
tss2 = "Fri Jun 21 13:22:37 +0800 2019"
timeArray = time.strptime(tss2, "%a %b %d %H:%M:%S %z %Y")
# timeArray可以调用tm_year等
print(timeArray.tm_year)   # 2019
