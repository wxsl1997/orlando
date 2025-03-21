import ssl
from urllib import request

# 忽略SSL证书验证
# noinspection PyUnresolvedReferences,PyProtectedMember
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    url = 'https://bkimg.cdn.bcebos.com/pic/b21bb051f819861841bb490948ed2e738ad4e6bb'
    request.urlretrieve(url, filename="/tmp/pic.png")
