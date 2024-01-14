import getpass
import adduser
import del_user
import login
import password
while True:
    print("Choose what do you want to do:\n")
    print("1.ADD USER")
    print("2. DELETE USER")
    print("3.LOGIN")
    print("4.CHANGE PASSWORD")
    print("5.EXIT")
    choice=int(input("ENTER your choice(1-5):"))
    if choice==1:
        username = input("Enter new username: ")
        real_name = input("Enter real name: ")
        new_password = getpass.getpass("Enter password: ")
        adduser.add_user(username, real_name,new_password)

    elif choice==2:
         username = input("Enter username to delete: ")
         del_user.delete_user(username)

    elif choice==3:
        username = input("User: ")
        passwords = input("Password: ")
        login.login_user(username, passwords)

    elif choice==4:
        username = input("Enter username: ")
        current_password = input("Current Password: ") 
        new_password = input("New Password: ")  
        confirm_password = input("Confirm password: ")

        if new_password == confirm_password:
            password.change_password(username, current_password, new_password)
        else:
            print("Passwords do not match. Nothing changed.") 
    elif choice==5:
        print("Exiting.....THANK YOU!!!")
        break
    else:
        print("Please input a number from 1 to 5.")
