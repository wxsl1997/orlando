import requests
import urllib3
from lxml import etree

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
        print(f'error occur when test request get, error: {e}')
    return result


if __name__ == '__main__':
    url = 'https://redis.io/pricing/'
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}
    txt = run_request(url, headers)
    html = etree.HTML(txt)

    # 提取价格对比栏
    compare_plan_header = html.xpath("/html/body/div[2]/div/div[3]/div/div/div/div")[0]
    # print(etree.tostring(compare_plan_header).decode('utf-8'))

    for div in compare_plan_header:
        # 产品版本 (注:xpath 索引从1开始)
        product = div.xpath("string(.//div/p[1])")
        # 产品价格
        price = div.xpath("string(.//div/p[2])")

        if product and price:
            print(f'{product:12s}| {price}')
