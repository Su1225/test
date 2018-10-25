"""

定以一个学生类，用来形容学生

"""

class Student():
    pass

mingyue = Student()

class PythonStudent():

    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("I 在做作业")

        # 推荐在函数末尾使用return语句
        return None
# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()
