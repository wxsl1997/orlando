import json

from practice.sms.model.student import Student
from practice.sms.service.studentService import StudentService


class App:
    studentService = StudentService()

    def run(self):
        self.show_menu()
        while True:
            choice = input("请选择:")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.del_student()
            elif choice == "3":
                self.modify_student()
            elif choice == "4":
                self.find_by_name()
            elif choice == "5":
                self.list_student()
            elif choice == "0":
                break
            else:
                print("tip:选择无效")

            input("按任意继续...")

    def list_student(self):
        students: list[Student] = self.studentService.list_student()
        self.show_student(students)

    def find_by_name(self):
        name = input("查询学员 姓名:")
        stu = self.studentService.find_by_name(name)
        self.show_student([]) if stu is None else self.show_student([stu])

    def modify_student(self):
        data = input("修改学员 格式:{name, gender, tel}")

        stu = Student()
        stu.__dict__ = json.loads(data)
        self.studentService.modify_student(stu)

    def del_student(self):
        name = input("删除学员 姓名:")
        self.studentService.del_student(name)

    def add_student(self):
        # {"name":"zhangSan","gender":"man","tel":"123xxx8888"}
        data = input("添加学员 格式:{name, gender, tel}")

        stu = Student()
        stu.__dict__ = json.loads(data)
        self.studentService.add_student(stu)

    @staticmethod
    def show_student(students):
        print('姓名\t性别\t手机号')
        # 暂无数据
        if len(students) == 0:
            print("   暂无数据   ")
        # 展示数据
        for stu in students:
            print(f"{stu.name}\t{stu.gender}\t {stu.tel}")

    @staticmethod
    def show_menu():
        print('功能列表')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员')
        print('4:查询学员')
        print('5:显示所有')
        print('0:退出系统')
