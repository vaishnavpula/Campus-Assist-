Students=[]
value = []
class Student:
    
    def __init__(self,name,age,roll,dept,sec,type):
        self.Name = name
        self.Age = age
        self.Roll = roll
        self.Dept = dept
        self.Sec = sec
        self.Type = type
    def display(self):
        
        global Students,value
        value.append(self.Name)
        Students.append(self)
    