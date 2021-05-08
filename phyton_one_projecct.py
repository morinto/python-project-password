# Login system for users

username = input("Enter username: ")

if username == "admin":
    pwd = input("enter password: ")
    if pwd == "password":
        print("Welcome")
    elif pwd == "":
        print("Cancelled")
    else:
        print("Wrong password")
elif username == "":
    print("Cancelled")
else:
    print("You are not a member")