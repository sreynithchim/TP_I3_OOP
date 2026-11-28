
class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name + "!")

name = input("Enter your name: ")
Greeting(name).say_hello()



