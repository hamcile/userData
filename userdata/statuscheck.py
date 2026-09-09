from getuser import getUserData, userData #type: ignore



def checkUserStatus():
    """this function check if the user is a new user or not. if he is, we would call the getUserdata function and if he is an already exiting user, we tell him his details are already stored"""
    print("ARE YOU A NEW USER?")
    newUser: bool = True
    while newUser:
        
        checkSatus: str = input("YES OR NO: ").lower().strip()
        if checkSatus == "yes":
            print ("LETS GET YOUR REGISTERED.")
            getUserData()
            print("Your details have been saved successfully.\n")
            print("ARE YOU A NEW USER?")
        elif checkSatus == "no":
            print("You Are a Member Already, Glad To See You Again.")
            newUser = False
        else:
            print("Choose Either Yes or No.")

def main():
    """this is used to test our program"""
    checkUserStatus()
    print(len(userData))
    for user in userData:
        print (user.greet())

main()
    