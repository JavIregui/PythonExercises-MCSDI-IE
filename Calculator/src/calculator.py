def menu():
    """ Displays the calculator menu options to the user 
        Arguments:
            None
        Returns:
            None
    """
    print("PYTHON CALCULATOR")
    print("-----------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("-----------------")
    
def get_user_choice() -> int:
    """ Gets the user's choice from the menu 
        Arguments:
            None
        Returns:
            int: The user's choice as an integer"""
    choice = input("Enter your choice (1-4): ")
    return int(choice)

def get_numbers() -> tuple[float, float]:
    """ Gets two numbers from the user 
        Arguments:
            None
        Returns:
            tuple: A tuple containing two float numbers entered by the user
    """
    numX = float(input("Enter the first number: "))
    numY = float(input("Enter the second number: "))
    return numX, numY

def clear_screen():
    """ Clears the console screen 
        Arguments:
            None
        Returns:
            None
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
def add(numX: float, numY: float) -> float:
    """ Adds two numbers 
        Arguments:
            numX (float): The first number
            numY (float): The second number
        Returns:
            float: The sum of the two numbers
    """
    return numX + numY

def subtract(numX: float, numY: float) -> float:
    """ Subtracts the second number from the first 
        Arguments:
            numX (float): The first number
            numY (float): The second number
        Returns:
            float: The difference between the two numbers
    """
    return numX - numY

def multiply(numX: float, numY: float) -> float:
    """ Multiplies two numbers 
        Arguments:
            numX (float): The first number
            numY (float): The second number
        Returns:
            float: The product of the two numbers
    """
    return numX * numY

def divide(numX: float, numY: float) -> float | None:
    """ Divides the first number by the second 
        Arguments:
            numX (float): The first number
            numY (float): The second number
        Returns:
            float | None: The quotient of the two numbers, or None if division by zero is attempted
    """
    if numY == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return numX / numY


choice:int
num1:float
num2:float
exit_program:bool = False

while not exit_program:
    menu()
    choice = get_user_choice()
    clear_screen()
    num1, num2 = get_numbers()
    match choice:
        case 1:
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        case 2:
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        case 3:
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        case 4:
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {num1} / {num2} = {result}")
        case _:
            print("Invalid choice. Please select a valid option.")
    
    exit_choice = input("Do you want to perform another calculation? (y/n): ")
    if exit_choice.lower() != 'y':
        exit_program = True
    else:
        clear_screen()
        
