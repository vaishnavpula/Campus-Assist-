class Python:
    def __init__(self,q,o,a):
        
       self.que = q
       self.opt = o
       self.ans = a
    def start(self):
        marks = 0
        for i in range(len(self.que)):
            print(self.que[i])
            for key,value in self.opt[i].items():
                print(key,value)
            while True:    
                    try:
                        select = input("Select any option(A,B,C,D):")
                        if select not in ["A","B","C","D"]:
                            raise ValueError("Invalid option")
                            break
                    except ValueError as e:
                            print(e)
                            select = input("Enter again(A,B,C,D):")
                    if select == self.ans[i]:
                        print("Correct")
                        marks+=1
                        break
                    else:
                        print("Wrong")
                        break
                        
                                
        print(f"Marks : {marks}/5")
                    
                    
        