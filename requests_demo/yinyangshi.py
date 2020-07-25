"""
AUTHOR:         zeng_xiao_yu
GITHUB:         https://github.com/zengxiaolou
EMAIL:          zengevent@gmail.com
TIME:           2020/7/25-09:35
INSTRUCTIONS:   爬取阴阳师壁纸官网中的2732 x 2048的壁纸
"""
from pathlib import Path
import re

import requests

url = "https://yys.163.com/media/picture.html"
html = requests.get(url)
pattern = re.compile(r'<a class="target" href="(.*?)" target="_blank">2732x2048</a>')
res = pattern.findall(html.text)
path = Path(__file__).parent
print(path)
j = 0
for i in res:
    j += 1
    img_path = str(path) + '/BGI/' + str(j) + '.png'
    res = requests.get(i)
    print("starting")
    with open(img_path, 'ab') as f:
        f.write(res.content)
        f.close()