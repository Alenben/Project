class college:
    def __init__(self,studentname,studentage):
        self.studentname=studentname
        self.studentage=studentage
class department:
    def __init__(self,studentname,departmentname):
        self.studentname=studentname
        self.departmentname=departmentname
        print("The student details are")
p1=college("alen",21)
p2=department("alen","Information Technology")
print(p1.studentname,p1.studentage)
print(p2.studentname,p2.departmentname)

