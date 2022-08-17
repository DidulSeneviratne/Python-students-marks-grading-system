# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 

# Any code taken from other sources is referenced within my code solution. 

# Student ID: w1899304……………………..… 
 
# Date: 02/04/2022……………………..…
def Part2():
        marks = ["0","20","40","60","80","100","120"]
        p = "Progress"
        t = "Progress(moduel trailer)"
        r = "Do not progress-moduel retriever"
        e = "Exclude"
        global P
        global T
        global R
        global E
        global Total
        global PList
        global TList
        global RList
        global EList
        # These values are taken for the count how many in each section and count the total outcomes
        P = 0
        T = 0
        R = 0
        E = 0
        Total = 0
        # These lists are create for the print stars as a downwards
        PList = []
        TList = []
        RList = []
        EList = []
        count = 0
        def grade():
                global P
                global T
                global R
                global E
                global Total
                global PL
                global TList
                global RList
                global EList
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
                            PList.append("*")
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
                            TList.append("*")
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
                            RList.append("*")
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
                            RList.append("*")
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
                            EList.append("*")
                        elif int(Defer) + int(Fail) >80 or int(Defer) + int(Fail) <80:
                            print("Total incorrect")
                            print("")
                        else:
                            print(r)
                            print("")
                            R += 1
                            Total += 1
                            RList.append("*")
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
                            EList.append("*")
                        elif int(Defer) + int(Fail) >100 or int(Defer) + int(Fail) <100:
                            print("Total incorrect")
                            print("")
                        else:
                            print(r)
                            print("")
                            R += 1
                            Total += 1
                            RList.append("*")
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
                            EList.append("*")
                        elif int(Defer) + int(Fail) >120 or int(Defer) + int(Fail) <120:
                            print("Total incorrect")
                            print("")
                        else:
                            print(r)
                            print("")
                            R += 1
                            Total += 1
                            RList.append("*") 
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
                        answer = input("Enter 'y' for yes or 'q' to quit and view results:- ")
                        answer = answer.lower()
                        while answer != "y" and answer != "q":
                                answer = input("Re-enter 'y' for yes or 'q' to quit or view results:- ")
                                answer = answer.lower()
                        if answer == "y":
                                pass
                        elif answer == "q":
                                break
                if len(PList) == len(TList):
                    pass
                elif len(PList) < len(TList):
                    while len(PList) != len(TList):
                        PList.append("")
                elif len(PList) > len(TList):
                    while len(PList) != len(TList):
                        TList.append("")
                if len(RList) == len(EList):
                    pass
                elif len(RList) < len(EList):
                    while len(RList) != len(EList):
                        RList.append("")
                elif len(RList) > len(EList):
                    while len(RList) != len(EList):
                        EList.append("")
                if len(PList) == len(RList):
                    pass
                elif len(PList) < len(RList):
                    while len(PList) != len(RList):
                        PList.append("")
                        TList.append("")
                elif len(PList) > len(RList):
                    while len(PList) != len(RList):
                        RList.append("")
                        EList.append("")
                print("")
                print("---------------------------------------------------------------------------")
                print("Vertical Histrogram")
                print("Progress |" ,end=" ")
                print("Traling |" ,end=" ")
                print("Retriever |" ,end=" ")
                print("Excluded")
                for i in PList or TList or RList or EList:
                    print(PList[count] ,end="            ")
                    print(TList[count] ,end="            ")
                    print(RList[count] ,end="            ")
                    print(EList[count])
                    count += 1
                print("")
                print(Total ,"outcomes in total")
                print("---------------------------------------------------------------------------")
            
