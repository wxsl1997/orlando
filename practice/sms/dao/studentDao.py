import json

from practice.sms.model.student import Student

DATA_PATH = "data/student.json"


class StudentDao:

    def add_student(self, stu: Student):
        students = self.list_student()
        # 新增
        students.append(stu)
        # 保存结果
        self.__save_students(students)

    def del_student(self, name: str):
        students = self.list_student()
        # 删除
        for stu in students:
            if stu.name == name:
                students.remove(stu)
                break
        # 保存结果
        self.__save_students(students)

    def modify_student(self, stu: Student):
        students = self.list_student()
        # 修改
        for item in students:
            if item.name == stu.name:
                item.gender = stu.gender
                item.tel = stu.tel
                break
        # 保存结果
        self.__save_students(students)

    def find_by_name(self, name: str):
        students = self.list_student()
        for stu in students:
            if stu.name == name:
                return stu

    @staticmethod
    def list_student():
        f = open(DATA_PATH, "r")
        data = json.load(f)
        f.close()
        return [Student(item["name"], item["gender"], item["tel"]) for item in data]

    @staticmethod
    def __save_students(students: list[Student]):
        f = open(DATA_PATH, "w")
        data = [stu.__dict__ for stu in students]
        f.write(json.dumps(data))
        f.close()
