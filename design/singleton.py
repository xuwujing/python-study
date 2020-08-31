
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                Singleton._instance = Singleton(*args, **kwargs)
                return Singleton._instance
def task(arg):
    obj = Singleton.instance()
    print("Task {}".format(arg), id(obj))


for i in range(10):
    t = threading.Thread(target=task, args=[i,])
    t.start()