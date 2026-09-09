from nameobj import User #type: ignore

userData: list = []

def getUserData() -> list:
    """this function takes in user inputs, cleans it up and stores in a list and returns a list of user datails."""
    name = ""
    age = 0
    while True:
        try:
            name = input("Enter Your Name: ").strip().lower()
            break
        except ValueError:
            print("Enter a Valid Name.")
    while True:
        try: 
            age = int(input("Enter Your Age: "))
            break
        except ValueError:
            print("Enter a Valid Number.\n")

    thisUser: User = User(name, age)
    userData.append(thisUser)
    return userData