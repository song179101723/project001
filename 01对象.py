__author__ = 'Jimmy'
class Student:  # 类名首字母大写
    company = 'IBM'
    count = 0
    def __init__(self, name, score):  # 构造方法;初始化
        self.name = name
        self.score = score
        Student.count = Student.count + 1
    def say_score(self):  # self必须位于第一个参数
        print("{0}的分数是：{1}".format(self.name, self.score))
        print("我的公司是：",Student.company)
        print(Student.count)
#print(type(Student("张三", 30)))
s1 = Student("张三", 30)  # 通过类名（）调用构造函数
print(type(s1))
# s1.age = 32   # 对象
# s1.salary = 3000  # 对象
s1.say_score()
# Student.say_score(s1)
# print(s1.age,s1.salary)
s2 = Student("张新", 40)
s2.say_score()
#  print(dir(s1)) # 可以获取对象的所有属性、方法
print(s1.__dict__) # 对象的属性字典
#备注
#备注2222
#备注33333
#备注本地-远程
#备注远程-本地
