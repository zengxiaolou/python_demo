"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/5/22-11:05
"""
import time
import sys
import stomp


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


conn = stomp.Connection()
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)

conn.subscribe(destination='/queue/test', id=1, ack='auto')
conn.send(body=' '.join(sys.argv[1:]), destination='/queue/tst')
time.sleep(2)
conn.disconnect()