"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/5/29-16:19
"""

a = {
    "name": "张三",
    "age": 18
}

b = {"gender": "男"}

c = None

a.update(b)
print(a)
a.update(c)
print(a)