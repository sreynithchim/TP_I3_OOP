class LuckyNumberGame:
    """Cheater game: the 'lucky' number is always the input plus one."""
    def __init__(self, number):
        self.number = number

    def get_next_number(self):
        return self.number + 1

    def get_result(self):
        result = self.get_next_number()
        return result
"""Note : User will nerver win the game because the next number is always the input plus one."""
while True:
    try:
        number = int(input("Please enter an Number : "))
        game = LuckyNumberGame(number)

    except ValueError:
        print("\n\n")
        print("Please enter a valid integer")

    else:
        print("\n\n")
        print(f"The next number is: {game.get_result()}")

    finally:
        print("\n\n")
        print("Do you want to play again? ")
        play_again = ['yes', 'no']
        answer = None
        while answer not in play_again:
            answer = input("Please enter (Yes/No): ").lower()
            if (answer == "no"):
                break
        if answer == 'no':
            break
        