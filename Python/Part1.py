# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 

# Any code taken from other sources is referenced within my code solution. 

# Student ID: w1899304……………………..… 
 
# Date: 02/04/2022……………………..… 
def Part1():
        marks = ["0","20","40","60","80","100","120"]
        p = "Progress"
        t = "Progress(moduel trailer)"
        r = "Do not progress-moduel retriever"
        e = "Exclude"
        # These values are taken for the count how many in each section and count the total outcomes 
        global P
        global T
        global R
        global E
        global Total
        P = 0
        T = 0
        R = 0
        E = 0
        Total = 0
        def grade():
                global P
                global T
                global R
                global E
                global Total
                print("")
                Pass = input("Enter your PASS credits:- ")
                if not Pass.isdigit():
                        try:
                            Pass = int(Pass)
                        except ValueError:
                            print("Integer required")
                            print("")
                elif Pass not in marks:
                    print("Out of range")
                    print("")
                elif Pass == "120":
                    Defer = input("Enter your DEFER credits:- ")
                    if not Defer.isdigit():
                            try:
                                Defer = int(Defer)
                            except ValueError:
                                print("Integer required")
                                print("")
                    elif Defer not in marks:
                        print("Out of range")
                        print("")
                    else:
                        Fail = input("Enter your FAIL credits:- ")
                        if not Fail.isdigit():
                                try:
                                    Fail = int(Fail)
                                except ValueError:
                                    print("Integer required")
                                    print("")
                        elif Fail not in marks:
                            print("Out of range")
                            print("")
                        elif int(Fail) + int(Defer) > 0 or int(Fail) + int(Defer) < 0:
                            print("Total incorrect")
                            print("")
                        else:
                            print(p)
                            print("")
                            P += 1
                            Total += 1
                elif Pass == "100":
                    Defer = input("Enter your DEFER credits:- ")
                    if not Defer.isdigit():
                            try:
                                Defer = int(Defer)
                            except ValueError:
                                print("Integer required")
                                print("")
                    elif Defer not in marks:
                        print("Out of range")
                        print("")
                    else:
                        Fail = input("Enter your FAIL credits:- ")
                        if not Fail.isdigit():
                                try:
                                    Fail = int(Fail)
                                except ValueError:
                                    print("Integer required")
                                    print("")
                        elif Fail not in marks:
                            print("Out of range")
                            print("")
                        elif int(Defer) + int(Fail) > 20 or int(Defer) + int(Fail) < 20:
                            print("Total incorrect")
                            print("")
                        else:
                            print(t)
                            print("")
                            T += 1
                            Total += 1
                elif Pass == "80":
                    Defer = input("Enter your DEFER credits:- ")
                    if not Defer.isdigit():
                            try:
                                Defer = int(Defer)
                            except ValueError:
                                print("Integer required")
                                print("")
                    elif Defer not in marks:
                        print("Out of range")
                        print("")
                    else:
                        Fail = input("Enter your FAIL credits:- ")
                        if not Fail.isdigit():
                                try:
                                    Fail = int(Fail)
                                except ValueError:
                                    print("Integer required")
                                    print("")
                        elif Fail not in marks:
                            print("Out of range")
                            print("")
                        elif int(Fail) + int(Defer) > 40 or int(Fail) + int(Defer) < 40:
                            print("Total incorrect")
                            print("")
                        else:
                            print(r)
                            print("")
                            R += 1
                            Total += 1
                elif Pass == "60":
                    Defer = input("Enter your DEFER credits:- ")
                    if not Defer.isdigit():
                            try:
                                Defer = int(Defer)
                            except ValueError:
                                print("Integer required")
                                print("")
                    elif Defer not in marks:
                        print("Out of range")
                        print("")
                    else:
                        Fail = input("Enter your FAIL credits:- ")
                        if not Fail.isdigit():
                                try:
                                    Fail = int(Fail)
                                except ValueError:
                                    print("Integer required")
                                    print("")
                        elif Fail not in marks:
                            print("Out of range")
                            print("")
                        elif int(Fail) + int(Defer) > 60 or int(Fail) + int(Defer) < 60:
                            print("Total incorrect")
                            print("")
                        else:
                            print(r)
                            print("")
                            R += 1
                            Total += 1
                elif Pass == "40":
                    Defer = input("Enter your DEFER credits:- ")
                    if not Defer.isdigit():
                            try:
                                Defer = int(Defer)
                            except ValueError:
                                print("Integer required")
                                print("")
                    elif Defer not in marks:
                        print("Out of range")
                        print("")
                    else:
                        Fail = input("Enter your FAIL credits:- ")
                        if not Fail.isdigit():
                                try:
                                    Fail = int(Fail)
                                except ValueError:
                                    print("Integer required")
                                    print("")
                        elif Fail not in marks:
                            print("Out of range")
                            print("")
                        elif Defer == "0":
                            print(e)
                            print("")
                            E += 1
                            Total += 1
                        elif int(Defer) + int(Fail) >80 or int(Defer) + int(Fail) <80:
                            print("Total incorrect")
                            print("")
                        else:
                            print(r)
                            print("")
                            R += 1
                            Total += 1
                elif Pass == "20":
                    Defer = input("Enter your DEFER credits:- ")
                    if not Defer.isdigit():
                            try:
                                Defer = int(Defer)
                            except ValueError:
                                print("Integer required")
                                print("")
                    elif Defer not in marks:
                        print("Out of range")
                        print("")
                    else:
                        Fail = input("Enter your FAIL credits:- ")
                        if not Fail.isdigit():
                                try:
                                    Fail = int(Fail)
                                except ValueError:
                                    print("Integer required")
                                    print("")
                        elif Fail not in marks:
                            print("Out of range")
                            print("")
                        elif Defer <= "20":
                            print(e)
                            print("")
                            E += 1
                            Total += 1
                        elif int(Defer) + int(Fail) >100 or int(Defer) + int(Fail) <100:
                            print("Total incorrect")
                            print("")
                        else:
                            print(r)
                            print("")
                            R += 1
                            Total += 1
                else:
                    Defer = input("Enter your DEFER credits:- ")
                    if not Defer.isdigit():
                            try:
                                Defer = int(Defer)
                            except ValueError:
                                print("Integer required")
                                print("")
                    elif Defer not in marks:
                        print("Out of range")
                        print("")
                    else:
                        Fail = input("Enter your FAIL credits:- ")
                        if not Fail.isdigit():
                                try:
                                    Fail = int(Fail)
                                except ValueError:
                                    print("Integer required")
                                    print("")
                        elif Fail not in marks:
                            print("Out of range")
                            print("")
                        elif Defer <= "40":
                            print(e)
                            print("")
                            E += 1
                            Total += 1
                        elif int(Defer) + int(Fail) >120 or int(Defer) + int(Fail) <120:
                            print("Total incorrect")
                            print("")
                        else:
                            print(r)
                            print("")
                            R += 1
                            Total += 1
        print("1:- Student version" "\n""2:- Staff version")
        ver = int(input("Please select your version:- "))
        while ver != 1 and ver != 2:
                ver = int(input("Please re-select your version:- "))
        if ver==1:
                print("Student Version")
                grade()
        elif ver==2:
                print("Staff Version with Histogram")
                while True:
                        grade()
                        print("Would you like to enter another set of data?")
                        answer = input("Enter 'y' for yes or 'q' to quit or view results:- ")
                        answer = answer.lower()
                        while answer != "y" and answer != "q":
                                answer = input("Re-enter 'y' for yes or 'q' to quit or view results:- ")
                                answer = answer.lower()
                        if answer == "y":
                                pass
                        elif answer == "q":
                                break
                print("")
                print("---------------------------------------------------------------------------")
                print("Horizontal Histrogram")
                print(P, p , ":" , "*"*P)
                print(T, t , ":" , "*"*T)
                print(R, r , ":" , "*"*R)
                print(E, e , ":" , "*"*E)
                print("")
                print(Total ,"outcomes in total")
                print("---------------------------------------------------------------------------")

        
            
            


        
    
