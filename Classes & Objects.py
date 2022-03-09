class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def check_pass(self):
        if self.marks >= 0 and self.marks <= 100:
            if self.marks >= 40:
                return 'Passed'
            else:
                return 'Failed'

student1 = Student('Alex', 90)
print(student1.name)
print(student1.marks)

verdict = student1.check_pass()
print(verdict)