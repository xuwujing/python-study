# 日志记录实现
import logging
# 设置日志最低级别为debug
#logging.basicConfig(level=logging.DEBUG)
# 设置日志的输出格式
#logging.basicConfig(format='%(asctime)s %(message)s')
# 设置日志的输出名称
logging.basicConfig(filename='example.log')

logging.info('hello')
logging.warning('good luck')
logging.error('%s,你好', 'pancm')

log = logging.getLogger('pancm')
# 生成一个StreamHandler，这个Handler可以将日志输出到console中
sh = logging.StreamHandler()
# 生成一个Formatter对象，使输出日志时只显示Logger名称和日志信息
fmt = logging.Formatter(fmt='%(name)s - %(message)s')
# 设置Formatter到StreamHandler中
sh.setFormatter(fmt)
# 将Handler添加到Logger中
log.addHandler(sh)
child_logger = logging.getLogger('pancm.child')
# 可以看到两个Logger输出的日志信息都使用了相同的日志格式
log.warning('hello')
child_logger.warning('hello')



