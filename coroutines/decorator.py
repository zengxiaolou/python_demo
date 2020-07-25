"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/5/13-11:30
"""
# def dubug(func):
#     def wrapper():
#         print("[DEBUG]: enter {}()".format(func.__name__))
#         return func()
#     return wrapper
#
# @dubug
# def hello():
#     print("hello")


# def logging(level):
#     def outwrapper(func):
#         def wrapper(*args, **kwargs):
#             print("[{0}]:enter{1}()".format(level, func.__name__))
#             return func(*args, **kwargs)
#         return wrapper
#     return outwrapper
#
# @logging(level="info")
# def hello(a,b,c):
#     print(a,b,c)
#
# hello('hello', 'good', 'morning')


# def test(level):
#     def outwrapper(func):
#         def wrapper(*args, **kwargs):
#             if level == 'info':
#                 print("这是消息提示")
#             elif level == 'warning':
#                 print("这是警告")
#             return func(*args, **kwargs)
#         return wrapper
#     return outwrapper
#
#
# @test('warning')
# def test1(f,g):
#     print(f + g)
#
# test1(1,2)

class logging(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[DEBUG]: enter {}()".format(func.__name__))
            return func(*args, **kwargs)
        return wrapper

@logging("info")
def hello(a, b, c):
    print(a, b, c)


hello("hello", "good", "morning")
