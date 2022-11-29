class Student:
    marks = []
    def getData(self, rn, name, m1, m2, m3):
        Student.rn = rn
        Student.name = name
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)
        
    def displayData(self):
        print ("Roll Number is: ", Student.rn)
        print ("Name is: ", Student.name)
        print ("Marks are: ", Student.marks)
        

        
r = int (input("Enter the roll number: "))
name = input("Enter the name: ")
m1 = int (input("Enter the marks in the first subject: "))
m2 = int (input("Enter the marks in the second subject: "))
m3 = int (input("Enter the marks in the third subject: "))

s1 = Student()
s1.getData(r, name, m1, m2, m3)
s1.displayData()
