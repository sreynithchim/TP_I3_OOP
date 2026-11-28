     
from tp02_1_greeting import Greeting
from tp02_2_rectangle import rectangle   # check the real class name
from tp02_3_equation import EquationCalculator
from tp02_4_hundreds_counter import HundredsCounter
from tp02_5_lucky_number import LuckyNumberGame


def show_menu():
    """Display the menu options."""
    print("========== TP02 Python OOP ==========")
    print("1. Greeting")
    print("2. Rectangle")
    print("3. Equation Calculator")
    print("4. Hundreds Counter")
    print("5. Lucky Number Game")
    print("0. Exit")
    print("=====================================")


while True:
    show_menu()
    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 0:
        print("Goodbye!")
        break
    elif choice == 1:
        Greeting(input("Enter your name : "))
    elif choice == 2:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        rectangle(width, height).result()
    elif choice == 3:
        y = float(input("Enter y : "))
        z = float(input("Enter z : "))
        EquationCalculator(y, z).display_result()
    elif choice == 4:
        number = int(input("Enter non-negative number : "))
        print("Complete hundreds : ", HundredsCounter(number).count_hundreds())
    elif choice == 5:
        number = int(input("Enter an integer : "))
        LuckyNumberGame(number).get_result()
    else:
        print("Invalid option. Please choose from 0 to 5.")
  