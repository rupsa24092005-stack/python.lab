class course :
    platform_name = 'CodeHere'
    total_courses = 0

    def __init__(self , course_name , inst_name , code , price):
        self.course_name = course_name 
        self.inst_name = inst_name
        self._code = code
        self.__price = price
        self.__student_enrolled = 0

        course.total_courses+=1
    def enrolled_students(self):
        self.__student_enrolled += 1
        print("Enrollment successful ")
    
    def get_price(self):
        return self.__price
    
    def set_price(self,new_price):
        if new_price >= 0 :
            self.__price = new_price
        else:
            print("Invalid Amount")
    def apply_discount(self,percent):
        discount_amount = (self.__price * percent ) / 100
        new_price = self.__price - discount_amount
        if new_price <= 0 :
            self.__price = new_price
            print("Discounted")
        else:
            print("Sorry Discount can't be applied")
    def display_course_info(self):
        print("CodeHere: ", course.platform_name)
        print("Course Name: ", self.course_name)
        print("Insturcter Name: ",self.inst_name)
        print("Course Code: ", self._code)
        print("Price", self.__price)
        print("Enrollment", self.__student_enrolled)

c1 = course("System Setup","John","SYS101",3000)
c2 = course("Python","Jonsan","PY102",7000)

c1.enrolled_students()
c1.enrolled_students()

c1.apply_discount(20)
c1.display_course_info()

print("Total Courses: ", course.total_courses)


