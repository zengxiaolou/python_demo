"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/5/12-17:57
"""


class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


head = Node('头', None)
last = head

for i in range(5):
    node = Node('v%s' % i, Node)
    last.next = node
    last = node

print(head.value)
print(head.next.value)