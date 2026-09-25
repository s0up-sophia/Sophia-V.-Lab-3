# Function that adds two numbers
def add(x, y):
    print(x+y)
# Function that subtracts two numbers
def subtract(x, y):
    print(x-y)
# Function that divides two numbers
def divide(x, y):
    print(x/y)
# Function that multiplies two numbers
def multiply(x, y):
    print(x*y)
# Function that quits the calculator
def quit():
    print("Thanks for using my calculator app! Shutting down...")
#Function that handles an invalid input
def invalid_input():
    print("Invalid input.Shutting down...")

#start of program
print("Welcome to my calculator app!")
print("what would you like to do?")
print("Type (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit: ")

user_choice= input(": ")

print(user_choice)

while(True):

    x = int(input("Enter the first number: "))
    y= int(input("Enter the second number: "))

    if user_choice == "a":
        add(x,y)
        break
    elif user_choice == "s":
        subtract(x,y)
        break
    elif user_choice == "d":
        divide(x,y)
        break
    elif user_choice == "m":
        multiply(x,y)
        break
    elif user_choice == "q":
        quit()
        break
    else:
        invalid_input()
        if user_choice in ["p","b","c","e","f","g","h","i","j","k","l","n","o","r","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9", "0"]:
            break