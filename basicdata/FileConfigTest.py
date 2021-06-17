# 配置文件读取

import configparser
import os
import yaml

cf = configparser.ConfigParser()
cf.read("C:\project\python\config\config.ini")  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块

secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，                        每个section由[]包裹，即[section])，并以列表的形式返回
print(secs)

options = cf.options("loggers")  # 获取某个section名为Mysql-Database所对应的键
print(options)

items = cf.items("loggers")  # 获取section名为Mysql-Database所对应的全部键值对
print(items)

host = cf.get("formatters", "keys")  # 获取[Mysql-Database]中host对应的值
print(host)



root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
cf2 = configparser.ConfigParser()
dir = root_dir+"/config/config.ini"
print(f'dir:{dir}')
cf2.read(dir)  # 拼接得到config.ini文件的路径，直接使用
secs2 = cf2.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，                        每个section由[]包裹，即[section])，并以列表的形式返回
print(secs2)

options2 = cf2.options("loggers")  # 获取某个section名为Mysql-Database所对应的键
print(options2)

items2 = cf2.items("loggers")  # 获取section名为Mysql-Database所对应的全部键值对
print(items2)

host2 = cf2.get("formatters", "keys")  # 获取[Mysql-Database]中host对应的值
print(host2)


cf3 = configparser.ConfigParser()
dir = root_dir+"/config/application-local.yml"
print(f'dir:{dir}')
# cf3.read(dir)
# secs3 = cf3.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，                        每个section由[]包裹，即[section])，并以列表的形式返回
# print(f'yml:{secs3}')


yamlPath = '../config/application-local.yml'
with open(yamlPath,'rb') as f:
    # yaml文件通过---分节，多个节组合成一个列表
    date = yaml.safe_load_all(f)
    # salf_load_all方法得到的是一个迭代器，需要使用list()方法转换为列表
    print(list(date))
