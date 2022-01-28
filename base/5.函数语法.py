import functools


# 元组
def sum_num(*args):
    """
    求和函数
    """
    assert (type(args) == tuple)
    # noinspection PyShadowingNames
    result = 0
    for num in args:
        result += num
    return result


assert sum_num(1, 2, 3) == 1 + 2 + 3


# 字典
def assign(**args):
    return args


assert assign(name="zhangRen", age=25) == {'name': 'zhangRen', 'age': 25}

# 全局变量
globalNum = 0


def change_num(value):
    global globalNum
    globalNum = value


# 赋值全局变量
change_num(5)
assert globalNum == 5

# lambda
assert (lambda **args: args)(name="zhangRen", age=25) == {'name': 'zhangRen', 'age': 25}

# 内置高阶函数
# map
result = map(lambda num: num ** 2, [1, 2, 3])
assert list(result) == [1, 4, 9]
# filter
result = filter(lambda num: num >= 2, [1, 2, 3])
assert list(result) == [2, 3]
# reduce
assert functools.reduce(lambda n1, n2: n1 + n2, [1, 2, 3]) == 6
