# 基础
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"__del__ {self}")

    def __str__(self):
        return str.format(f"user:(name={self.name}, age={self.age})")

    def get_age(self):
        return self.age


# 创建实例
user = User("zhangRen", 25)
# 调用方法
assert user.get_age() == 25
# 访问属性
assert user.age == 25
# 删除实例
del user


# 继承
class P1:
    def __init__(self):
        self.__name = "p1"
        print(f"__init__ {self.__name}")

    def get_name(self):
        return self.__name


class P2:
    def __init__(self):
        self.__name = "p2"
        print(f"__init__ {self.__name}")

    def get_name(self):
        return self.__name


class S1(P1, P2):

    def __init__(self):
        P1.__init__(self)
        P2.__init__(self)
        self.__name = "s1"
        print(f"__init__ {self.__name}")

    def get_name(self):
        return self.__name

    def get_p1_name(self):
        return P1.get_name(self)

    def get_p2_name(self):
        return P2.get_name(self)


s1 = S1()
assert s1.get_name() == 's1'
assert s1.get_p1_name() == 'p1'
assert s1.get_p2_name() == 'p2'

# 多态
