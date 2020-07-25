"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.comimport requests

TIME:    2020/5/12-15:23
"""
import requests


def download_image(url):
    """
    同步下载图片
    :param url:
    :return:
    """
    print("开始下载图片")
    response = requests.get(url)
    print("下载完成")
    file_name = url.rsplit('_')[-1]
    with open('./' + file_name, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    url_list = [
        'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
        'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
        'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
    ]
    for url in url_list:
        download_image(url)