import re

if __name__ == '__main__':
    txt = 'I love sport, I love study, I love sleep'

    # findall 查找
    result = re.findall(pattern=r's[a-z]*', string=txt, flags=re.IGNORECASE)
    print(result)
    # ['sport', 'study', 'sleep']

    # search 查找
    result = re.search(pattern=r'love', string=txt, flags=re.IGNORECASE)
    print(result)
    # <re.Match object; span=(2, 6), match='love'>
    print(result.group())
    # love
    print(result.span())
    # (2, 6)

    # split 切割
    result = re.split(r'\W+', txt)
    print(result)
    # ['I', 'love', 'sport', 'I', 'love', 'study', 'I', 'love', 'sleep']

    # compile 编译
    p = re.compile(r'[a-z]+', flags=re.IGNORECASE)
    result = p.findall(txt)
    print(result)
    # ['I', 'love', 'sport', 'I', 'love', 'study', 'I', 'love', 'sleep']
