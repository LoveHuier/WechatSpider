"""
    This is a wechat spider .
"""

import urllib.request


#模拟成浏览器
headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]

#将opener安装为全局
urllib.request.install_opener(opener)
