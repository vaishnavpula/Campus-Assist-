class Subjects:
    def __init__(self):
        self.subjects = ["Python", "Java", "DBMS", "AI", "ML"]

    def info(self):
        print("Student Grade Calculation :")
class Grade(Subjects):
    def __init__(self,a):
        super().__init__()
        self.marks = a
    def calculate(self):
        for i in self.subjects:
            self.mark = float(input("Enter the marks you scored in " + i + ": "))
            self.marks.append(self.mark)
        print(self.marks) 
        for j,k in zip(self.subjects,self.marks):
            print(j,k)
        
        avg =  sum(self.marks)/len(self.subjects) 
        if 90<=avg<100:
            G = "O"
            return G
        elif 70<=avg<90:
                G = "A+"
                return G
        elif 50<=avg<70:
                    G = "B+"
                    return G           
        elif 35<=avg<50:
                    G = "P"
                    return G   
        else:
            G = "F"
            return G
                      
               
             
        
    
    
    