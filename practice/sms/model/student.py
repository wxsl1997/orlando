class Student:
    def __init__(self, name=None, gender=None, tel=None):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f"student:(name={self.name}, gender={self.gender}, tel={self.tel})"
