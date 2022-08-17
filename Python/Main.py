# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 

# Any code taken from other sources is referenced within my code solution. 

# Student ID: w1899304……………………..… 
 
# Date: 02/04/2022……………………..…
print("""1. Horizontal histogram
2. Vertical histogram
3. List type
4. Text file""")
opt = int(input("Please select your output way:- "))
while opt != 1 and opt != 2 and opt != 3 and opt != 4:
    opt = int(input("Please re-select your output way:- "))
if opt == 1:
        print("Horizontal histogram")
        print("")
        import Part1
        Part1.Part1()
elif opt == 2:
        print("Vertical histogram")
        print("")
        import Part2
        Part2.Part2()
elif opt == 3:
        print("List type")
        print("")
        import Part3
        Part3.Part3()
else:
        print("Text file")
        print("")
        import Part4
        Part4.Part4()
        
