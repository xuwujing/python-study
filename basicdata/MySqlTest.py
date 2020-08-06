# mysql的连接和使用
import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.8.83",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456"  # 数据库密码
)

print(mydb)

