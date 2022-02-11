from practice.sms.dao.studentDao import StudentDao
from practice.sms.model.student import Student


class StudentService:
    studentDao = StudentDao()

    def add_student(self, stu: Student):
        db_stu = self.find_by_name(stu.name)
        if db_stu is not None:
            print("已经存在")
        else:
            self.studentDao.add_student(stu)
            print("操作成功")

    def del_student(self, name: str):
        stu = self.studentDao.find_by_name(name)
        if stu is None:
            print("查无此人")
        else:
            self.studentDao.del_student(name)
            print("操作成功")

    def modify_student(self, stu: Student):
        stu = self.studentDao.find_by_name(stu.name)
        if stu is None:
            print("查无此人")
        else:
            self.studentDao.modify_student(stu)
            print("操作成功")

    def find_by_name(self, name: str):
        return self.studentDao.find_by_name(name)

    def list_student(self):
        return self.studentDao.list_student()
