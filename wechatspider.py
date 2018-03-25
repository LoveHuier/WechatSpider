"""
    This is a wechat spider .
"""

import urllib.request
import urllib.error
import time

# 模拟成浏览器
headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]

# 将opener安装为全局
urllib.request.install_opener(opener)


def use_proxy(proxy_addr, url):
    """
    使用代理服务器的函数
    :param proxy_addr:代理IP
    :param url:起始页url
    :return:data
    """
    try:
        proxy = urllib.request.ProxyHandler({'http': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

        # 若为URLError异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        # 若为Exception异常，延时1秒
        time.sleep(1)
