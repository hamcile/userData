class User:
    def __init__(self, name: str, age: int):
        """this intialize out user's data for this project"""
        self.name = name
        self.age = age

    def greet(self):
        """returns a greeting with the user name and age when ever it is called."""
        return f"Hello! my name is {self.name} and I am {self.age} years old. what about you?"

u1: User = User("John", 16)

print(u1.greet())