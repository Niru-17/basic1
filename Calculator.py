art = """
    _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
    

def add(n1, n2):
            return n1 + n2

def subtract(n1, n2):
        return n1 - n2

def multiply(n1, n2):
        return n1 * n2

def divide(n1, n2):
        return n1 / n2

operations = {
        
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,

}
def calculator():
    print(art)
    should_continue = True
    first_number = float(input("What's Your First Number?:"))
    while should_continue:
        User_Operation = input("Pick an Operation:")
        second_number = float(input("What's Your Second Number?:"))
        final_answer = operations[User_Operation](first_number, second_number)
        print(f"{first_number} {User_Operation} {second_number} = {final_answer} ")
        user_pers = input("You want to continue?:")
        if user_pers == "y":
            first_number = final_answer
        elif user_pers == "n":
            user_pers2 = input("You want to restart?:")
            if user_pers2 == 'y':
                print("\n" * 24)    
                calculator()
            else:
                should_continue = False
                print("\n" * 100)    
                   
            

calculator()