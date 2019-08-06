def add(a, b):
    c = a + b
    print("Sum of {0} and {1} is {2}".format(a,b,c))

def multiply(a, b):
    c = a * b
    print("Product of {0} and {1} is {2}".format(a,b,c))

def divide(a, b):
    c = a / b
    print("Quotient of {0} and {1} is {2}".format(a,b,c))

def substract(a, b):
    c = a - b
    print("Difference of {0} and {1} is {2}".format(a,b,c))

def calculator():
    print("""                Welcome to Calculator built on Python!
                                Author: Nitin""")
    end = 1
    while end == 1:
            print("\n------------------------------------------------------------")
            print("1.Addition\n2.Multiplication\n3.Division\n4.Substraction\nChoose...")
            choice = int(input())
            for x in range(4):
                print("\n")
            if(choice == 1):
                print("Addition")
                print("Enter 2 numbers")
                a, b = int(input()), int(input())
                add(a,b)
            elif(choice == 2):
                print("Multiplication")
                print("Enter 2 numbers")
                a, b = int(input()), int(input())
                multiply(a,b)
            elif(choice == 3):
                print("Division")
                print("Enter 2 numbers")
                a, b = int(input()), int(input())
                divide(a,b)
            elif(choice == 4):
                print("Substraction")
                print("Enter 2 numbers")
                a, b = int(input()), int(input())
                substract(a,b)
            print("Again? 1, Exit? 2")
            end = int(input())
    print("\n------------------------------------------------------------")


calculator()
