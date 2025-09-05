"""
THis is a DOCSTRING, this decribes what the program does
This program is a calculator which takes inputs from the user, which is 
2 numbers and the required operator and gives output based on the supplied 
operator

"""

# function that returns a value
def calc(num1, num2, ops):
    # dictionary of operations
    operations = {"+": num1 + num2, "-": num1 - num2, "*": num1 * num2, "/": num1 / num2}
    return operations[ops]


new_num = True
while(True):
    if new_num:
        num1 = float(input("Whats the first number: "))
    ops = str(input("+\n-\n*\n/\nPick an operation: "))
    num2 = float(input("Whats the next number: "))

    res = calc(num1,num2,ops)
    print(f"{num1} {ops} {num2} = {res}")

    choice = input(f"Type 'y' to continue calculating with {res}, or type n to start a new calculation: ").lower()

    if choice == 'y':
        new_num = False
        num1 = res
    else:
        new_num = True

