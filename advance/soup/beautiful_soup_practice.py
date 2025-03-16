import requests
import urllib3
from bs4 import BeautifulSoup

UTF_8 = 'utf-8'


def run_request(url: str, headers=None):
    # disable https certificate verification warn
    urllib3.disable_warnings()
    result = None
    try:
        with requests.get(url=url, verify=False, headers=headers) as response:
            response.encoding = UTF_8
            result = response.text
    except Exception as e:
        print(f'error occur when test request get, error:{e}')
    return result


if __name__ == '__main__':
    url = 'https://www.shicimingju.com/chaxun/zuozhe/1.html'
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}
    txt = run_request(url, headers)

    soup = BeautifulSoup(txt, 'lxml')

    # print(soup.prettify())

    # 找到 ui > li 列表
    lis = soup.select(".list > ul >li")
    for li in lis:
        num = li.select_one(".num").get_text()
        link = li.select("a")[0].get("href")
        title = li.select("a")[0].get_text()
        print(f'num:{num:4s}| link:https://www.shicimingju.com/{link:36s}| title:{title}')
