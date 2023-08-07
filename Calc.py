def add(a, b):
    result = a+b
    print("result is "+ str(result))

def mul(a, b):
    result = a*b
    print("result is "+ str(result))

def sub(a, b):
    result = a-b
    print("result is "+ str(result))

def div(a, b):
    result = a/b
    print("result is "+ str(result))

loop = True

while loop:

    print("""input your choice:
    A. Addition
    B. Substraction
    C. Multiplication
    D. Division
    E. Exit""")

    choice = input().lower()


    if choice == "a":

        num1 = int(input("enter the first number: "))
        num2 = int(input("enter second number: ")) 
        add(num1, num2)
    elif choice == "b":
        
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter second number: "))
        sub(num1, num2)
    elif choice == "c":
        
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter second number: "))
        mul(num1, num2)
    elif choice == "d":
        
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter second number: ")) 
        div(num1, num2)
    elif choice == "e":
        print("Program ended")
        quit()    


    exit = input("do you want to exit Y/N: ").lower()
    if exit == "y":
        loop = False
    else:
        loop = True    

