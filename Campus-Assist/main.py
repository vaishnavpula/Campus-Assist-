from Student.Details.details import Student, Students, value
from Student.Expenses.charges import Prices, price
from Student.grade.cgpa import Grade
from Student.grade.quiz import Test
import os
if os.path.exists("Student_info.txt"):
    with open("Student_info.txt","r") as f:
        for line in f:
            line=line.strip()
            if line:
                name,age,roll,dept,sec,stype=line.split(",")
                s=Student(name,int(age),roll,dept,sec,stype)
                Students.append(s)
if os.path.exists("Student_expenses.txt"):
    with open("Student_expenses.txt","r") as f:
        for line in f:
            line = line.strip()
            if line:
                naam, bus_fee, stationaries, junk_food, mess_fee = line.split(",")
                v = Prices(naam,float(bus_fee),float(stationaries),float(junk_food),float(mess_fee))
                price.append(v)                
while True:
    choice = input("Enter the choice : ")

    if choice == '1':
        name = input("Enter name of student : ")
        age = int(input("Enter age : "))
        roll = input("Enter regd_no : ")
        dept = input("Enter department : ")
        sec = input("Enter the section : ")
        stype = input("Enter type(D/s - Hostel) : ")
        with open("Student_info.txt","a") as f:
                f.write(f"{name},{age},{roll},{dept},{sec},{stype}\n")
        s1 = Student(name, age, roll, dept, sec, stype)
        s1.display()

    elif choice == '2':
        print(value)

    elif choice == '3':
        key = input("Enter the name of a person : ")
        found = False

        for i in Students:
            if i.Name == key:
                print("Name :", i.Name)
                print("Age :", i.Age)
                print("Regd_no :", i.Roll)
                print("Department :", i.Dept)
                print("Section :", i.Sec)
                print("Type :", i.Type)
                found = True
                break
                
        if not found:
            print("No student with that Name")

    elif choice == '4':
        naam = input("Enter the name of person : ")
        found = False

        for i in Students:
            if i.Name == naam:
                found = True

                bus_fee = 0
                stationaries = 0
                junk_food = 0
                mess_fee = 0

                print("Enter the details of", naam)

                if i.Type == "D/s":
                    print("He is a Dayscholar")
                elif i.Type == "Hostel":
                    print("He is from Hostel")

                while True:
                    print("1. Transportation fee")
                    print("2. canteen")
                    print("3. Mess")
                    print("4. Exit")
                    a = input("Enter the category : ")

                    if a == '1':
                        bus_fee = int(input("Enter the bus fee : "))

                    elif a == '2':
                        print("-------------canteen------------")
                        print("1. stationaries")
                        print("2. food")
                        stationaries = int(input("Price spent on stationaries : "))
                        junk_food = int(input("Price spent on food : "))

                    elif a == '3':
                        mess_fee = int(input("Enter the mess fee : "))

                    elif a == '4':
                        break

                    else:
                        print("Invalid choice")
                with open("Student_expenses.txt","a") as f:
                    f.write(f"{naam},{bus_fee},{stationaries},{junk_food},{mess_fee}\n")
                s2 = Prices(naam, bus_fee, stationaries, junk_food, mess_fee)
                s2.spent()
                break

        if not found:
            print("No expenses found")

    elif choice == '5':
        source = input("Enter the name : ")
        found = False

        for j in price:
            if j.Name == source:
                found = True
                print("Name of student :", j.Name)
                print("Bus Fee :", j.Bus)
                print("Stationary items :", j.Stationary)
                print("On junk-food :", j.junk)
                print("Mess Fee :", j.Mess)

                total = j.Bus + j.Stationary + j.junk + j.Mess
                print("The total cost spent by", j.Name, "is :", total)
                break

        if not found:
            print("No student with that name")

    elif choice == '6':
        s3 = Test([], [], [])
        s3.display_test()

    elif choice == '7':
        search = input("Enter the name :")
        for i in Students:
            if i.Name == search:
                print("-----",i.Name+"'s","Score :","-----")
                s4 = Grade([])
                s4.info()
                value = s4.calculate()
                with open("Grade.txt","w") as f:
                                f.write(f"{i.Name} Scored grade {value}\n")
            print(value)
            
        

    else:
        print("Exited...")
        break