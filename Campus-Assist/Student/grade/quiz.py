from Student.grade.Python_que import Python
from Student.grade.Java_test import Java
class Type:
    def __init__(self):
        self.sub = ["Python","Java"]   
    
class Test(Type):
    def __init__(self,q,o,a):
        super().__init__()
       
        self.que = q
        self.opt= o
        self.answer = a
    def display_test(self):
        for i in self.sub:
           print(i)
           
        choice = int(input("Enter your choice type test:"))
        if choice == 1:
                    print("---------------------Python Test----------------------")
                    self.que = ["1. Which keyword is used to define a function in Python?","2. Which of the following is mutable?","3. Which data structure stores data in key-value pairs?","4. Which keyword is used to handle exceptions?","5. What is the index of the first element in a Python list?"]
                    self.opt = [{"A)":"function","B)":"def","C)":"fun","D)":"define"},{"A)":"tuple","B)":"string","C)":"list","D)":"integer"},{"A)":"list","B)":"tuple","C)":"dictionaries","D)":"strings"},{"A)":"except","B)":"try","C)":"catch","D)":"finally"},{"A)":"-1","B)":"0","C)":"1","D)":"4"}]
                    self.ans = ["B","C","C","A","B"]
                    p1 = Python(self.que,self.opt,self.ans)
                    p1.start()
                     
        elif choice == 2:
                    print("---------------------Java Test----------------------")
                    self.que = ["1. Which method is the starting point of a Java program?","2. Which keyword is used for inheritance in Java?","3. Which keyword is used to handle exceptions in Java?","4. Which keyword is used to create an object?","5. Which keyword is used to prevent inheritance?"]
                    self.opt = [{"A)":"start()","B)":"main()","C)":"run()","D)":"execute()"},{"A)":"inherits","B)":"extends","C)":"implements","D)":"super()"},{"A)":"try","B)":"catch","C)":"handle","D)":"error"},{"A)":"new","B)":"create","C)":"object","D)":"class"},{"A)":"static","B)":"private","C)":"final","D)":"const"}]
                    self.ans = ["B","B","B","A","C"]
                    j1 = Java(self.que,self.opt,self.ans)
                    j1.start()
                    