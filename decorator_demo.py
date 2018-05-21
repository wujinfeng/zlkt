from functools import wraps


# 装饰器实际上是一个函数
# 有2个特别之处
# 1.参数是一个函数
# 2.返回值是一个函数

# 在打印run之前，先要打印hello world
# 在所有的函数之前，都要打印一个hello world

# 1.装饰器使用是通过@符号，放在函数的上面
# 2.装饰器中定义的函数，要使用*args,**kwargs两对兄弟的组合，并且在执行
#   原始函数的时候也要把 *args,**kwargs传递进去
# 3.需要使用functions.wraps在装饰器中的函数把传进来的这个函数进行包裹，
#   这样不会丢失原来函数的__name__等属性

def my_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('hello world')
        func(*args, **kwargs)

    return wrapper


@my_log
def run():
    print('run')


@my_log
def add(a, b):
    print('add结果： %s' % (a + b))


run()
add(2, 3)
