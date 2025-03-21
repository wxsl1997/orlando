import scrapy
from bs4 import BeautifulSoup

from advance.scrapy.scrapy_case.scrapy_case.items import ScrapyCaseItem


class BiZhiSpider(scrapy.Spider):
    # 任务名称
    name = "wallpaper"
    # 目标网站
    allowed_domains = ["www.51miz.com"]
    # 目标页面
    start_urls = ["https://www.51miz.com/collections/meinurenwu/"]

    def parse(self, response, **kwargs):
        txt = response.body

        # open("page.html", "wb").write(response.body)

        soup = BeautifulSoup(txt, 'lxml')

        divs = soup.select(".wookmark > div")
        for div in divs:
            img = div.select_one(".image-box >img")
            print(img)

            # 提取 url
            link: str = img.get("data-original")
            url = link[0:link.index("!")]

            # 提取 title
            title = img.get("title")

            item = ScrapyCaseItem()
            # 传递属性
            item['title'] = title
            item['url'] = f"https:{url}"
            yield item
