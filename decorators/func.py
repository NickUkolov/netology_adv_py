from datetime import datetime


def logger(path):
    def logger_(function):
        def upd_function(*args, **kwargs):
            date = datetime.now().strftime("%b %d %Y %H:%M:%S")
            name = function.__name__
            args_ = args
            kwargs_ = kwargs
            result = function(*args, **kwargs)
            with open(path + 'data.txt', 'a') as file:
                file.write(f'{date}_/_{name}_/_{args_}_/_{kwargs}_/_{result}\n')
            return result
        return upd_function
    return logger_
