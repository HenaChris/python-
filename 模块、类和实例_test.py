####模块
print('恋习Python')
def main():
    print('恋习Python')
#在导入该模块到其他模块时，该部分不执行，可以用来测试
if __name__ == '__main__':
    main()
    print('跟着菜鸟分析，练习Python越练越恋')


####类
#括号里面填写继承了哪个类，object表示继承了object类
class Student(object):
    pass
bart = Student()
print(1,bart)
'''输出：<__main__.Student object at 0x000001AF22335320>'''
#自由绑定实例变量的属性
bart.name = 'Bart Simpson'
print(2,bart.name)


#__init__,创建实例的时候要传参
class Student(object):


    def __init__(self,name,score):
        self.name = name
        self.score = score
bart = Student('Bart Simpson',59)
print(3,bart)
print(4,bart.name,bart.score)
#数据的封装，用类的方法去访问数据
class Student(object):


    def __init__(self,name,score):
        self.name = name
        self.score = score


    def print_score(self):
        print("%s:%s"%(self.name,self.score))


    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson',59)
bart.print_score()
print(bart.get_grade())


####访问限制
#将gender设置为私有这样外部就没法通过bart.gender = 'female'来修改属性了，只能通过类的方法去修改
#也无法访问到私有属性。只能通过类的方法去访问。

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        print(self.__gender)
    def set_gender(self,gender):
        self.__gender = gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')