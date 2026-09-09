class User:
    def __init__(self, name: str, age: int):
        """this intialize out user's data for this project"""
        self.name = name
        self.age = age
        self.email = name + str(age) + "@gmail.com"

    def greet(self):
        """returns a greeting with the user name and age when ever it is called."""
        return f"Hello! my name is {self.name} and I am {self.age} years old. what about you?"

# userData: list = []

# def getUserData() -> list:
#     """this function takes in user inputs, cleans it up and stores in a list and returns a list of user datails."""
#     name = ""
#     age = 0
#     while True:
#         try:
#             name = input("Enter Your Name: ").strip().lower()
#             break
#         except ValueError:
#             print("Enter a Valid Name.")
#     while True:
#         try: 
#             age = int(input("Enter Your Age: "))
#             break
#         except ValueError:
#             print("Enter a Valid Number.\n")

#     thisUser: User = User(name, age)
#     userData.append(thisUser)
#     return userData
    

# getUserData()
# for user in userData:
#     print (user.name)


# def checkUserStatus():
#     """this function check if the user is a new user or not. if he is, we would call the getUserdata function and if he is an already exiting user, we tell him his details are already stored"""
#     print("ARE YOU A NEW USER?")
#     newUser: bool = True
#     while newUser:
        
#         checkSatus: str = input("YES OR NO: ").lower().strip()
#         if checkSatus == "yes":
#             print ("LETS GET YOUR REGISTERED.")
#             getUserData()
#             print("Your details have been saved successfully.\n")
#             print("ARE YOU A NEW USER?")
#         elif checkSatus == "no":
#             print("You Are a Member Already, Glad To See You Again.")
#             newUser = False
#         else:
#             print("Choose Either Yes or No.")
    
        


# def main():
#     """this is used to test our program"""
#     checkUserStatus()
#     print(len(userData))
#     for user in userData:
#         print (user.greet())

# main()

# '''while newUser:
#     print("ARE YOU A NEW USER?")
#     checkSatus: str = input("YES OR NO: ").lower().strip()
#     if checkSatus == "yes":
#         newUser = True
#         print ("LETS GET YOUR REGISTERED.")
#         userName: str = input("full name please: ").lower().strip()
#         age: int = int(input("what is your age: "))
        
#     elif checkSatus == "no":
#         newUser = False
#         print("YOUR DATA IS SAFE WITH US.")
#     elif checkSatus != "no" or checkSatus != "yes":
#         print("SELECT A VALID OPTION.")


#     person: User = User(userName, age)
#     userData.append(person)

# if newUser == False:
#     print(len(userData))
#     print(userData)'''