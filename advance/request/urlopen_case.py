import ssl
from urllib import request

UTF_8 = 'utf-8'
# 忽略SSL证书验证
# noinspection PyUnresolvedReferences,PyProtectedMember
ssl._create_default_https_context = ssl._create_unverified_context


def test_request(url: str, headers=None):
    try:
        req = request.Request(url=url, headers=headers)
        with request.urlopen(req, timeout=3_000) as response:
            data = response.read()
            print(data.decode(UTF_8))
    except Exception as e:
        print(f'error occur when test request {e}')


def test_urlopen(url: str):
    try:
        with request.urlopen(url) as response:
            data = response.read()
            print(data.decode(UTF_8))
    except Exception as e:
        print(f'error occur when test url open {e}')


if __name__ == '__main__':
    test_urlopen("https://www.baidu.com/")
    test_request("https://www.baidu.com/", {'cookie': 'SESSION=ZDk0ZTYwZDYtZWYzMi00NmI0LTlhNjUtOTM2ZjA1MmEzYTkx'})
