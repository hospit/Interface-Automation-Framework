from functools import wraps


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            print(self.logfile)
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        print('this is class function logging')
        pass
class log(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        #
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # print(self.logfile,'/n',log_string)
        # 现在，发送一个通知
        return self.func()

        # return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass

@logit()
def myfunc1(param):
    return param

print(myfunc1('this is function param'))