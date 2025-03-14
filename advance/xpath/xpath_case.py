from lxml import etree

if __name__ == '__main__':
    with open('page-01.html', 'r', encoding='utf-8') as file:
        txt = file.read()
        html = etree.HTML(txt)
        print(html)
        # <Element html at xxx>

        # 查找 id 是 special-remind 的元素
        result = html.xpath('/html/body/section/p[@id="special-remind"]/text()')
        print(result)
        # ['这是一个演示段落 ']

        # 查找 class 是 title 的元素
        result = html.xpath('//h2[@class="title"]/text()')
        print(result)
        # ['今日推荐']

        # 修正 html
        result = etree.tostring(html).decode('utf-8')
        # print(result)
