import requests
import urllib3

UTF_8 = 'utf-8'


def test_requests_get(url: str, headers=None):
    # disable https certificate verification warn
    urllib3.disable_warnings()
    try:
        with requests.get(url=url, verify=False, headers=headers) as response:
            response.encoding = UTF_8
            print(f'{url} response code:{response.status_code}')
            print(response.text)
            # 打印二进制内容
            # print(response.content)
            print(response.cookies)
    except Exception as e:
        print(f'error occur when test request get{e}')


def test_requests_post(url: str, json=None, headers=None):
    # disable https certificate verification warn
    urllib3.disable_warnings()
    try:
        with requests.post(url=url, json=json, verify=False, headers=headers) as response:
            response.encoding = UTF_8
            print(f'{url} response code:{response.status_code}')
            print(response.text)
    except Exception as e:
        print(f'error occur when test request post{e}')


if __name__ == '__main__':
    test_requests_get("http://httpbin.org/get")
    test_requests_post("http://httpbin.org/post", json={"k1": "v1"}, headers={"h1": "v1"})
