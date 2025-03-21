import os
import ssl
from urllib import request

# 忽略SSL证书验证
# noinspection PyUnresolvedReferences,PyProtectedMember
ssl._create_default_https_context = ssl._create_unverified_context

STORAGE_PATH = "/tmp/wallpaper/"


# noinspection PyMethodMayBeStatic
class ScrapyCasePipeline:

    def open_spider(self, spider):
        print(f'start open spider, spider:{spider.name}')

        exist = os.path.exists(STORAGE_PATH)
        if not exist:
            os.mkdir(STORAGE_PATH)
            print(f"success mk storage dir:{STORAGE_PATH}")

    def process_item(self, item, spider):
        title = item['title']
        url = item['url']

        print(f'start process item, spider:{spider.name}, item:{item}')

        filename = f"{STORAGE_PATH}{title}.jpeg"

        opener = request.build_opener()
        opener.addheaders = (
            [
                ("User-Agent",
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"),
                ("host", "img-qn-4.51miz.com"),
                ("referer", "https://www.51miz.com/")
            ]
        )
        request.install_opener(opener)

        request.urlretrieve(url, filename)
        print(f'end process item, spider:{spider.name}, item:{item}')
        return item

    def close_spider(self, spider):
        print(f'close spider, spider:{spider.name}')
