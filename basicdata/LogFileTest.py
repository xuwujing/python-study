# 日志文件配置读取测试
import logging
import logging.config
from sys import path

folder = "C:\project\python\config"
#log_path = "logging.conf"

log_path = f"{folder}/logging.conf"

log_file_path = path.join(path.dirname(path.abspath(__file__)), log_path)
#logging.config.fileConfig(log_file_path)
logging.config.fileConfig(log_path)
#logging.config.fileConfig(fname='logtest.conf', disable_existing_loggers=False)
logs = logging.getLogger('error')
logs.error('errorsssss')

