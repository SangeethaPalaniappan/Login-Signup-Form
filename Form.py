# User Details

import sys
sys.path.append(r'C:\Users\sange\Login-Signup-Form')

import Database as db


class Login:
    def login_details(self, mail, password):

        db_obj = db.Database()
        # Check the details 
        if db_obj.authenticate(mail, password) == 1:
            return "Login Successful"
        return "Given Credentials are not valid"
        

class Signup:
    def signup_details(self, first_name, last_name, email_id, password, contact_no):

       
        db_obj = db.Database()
        # store these details in the database

        if db_obj.add_details(first_name, last_name, email_id, password, contact_no) == 1:
            return "Account Created Successfully"
        
        return "Account already Exists"
    


def opt(option):
    if option == 2:
        login = Login()
        mail_id = input("Enter the Email : ")
        password = input("Enter the Password : ")
        # check from the database
        print(login.login_details(mail_id.lower(), password))

    elif option == 1:
        signup = Signup()
        first_name = input("First Name : ")
        last_name = input("Last Name : ")
        
        while True:
            email_id = input("Enter the Email : ")
            email = email_id[len(email_id) -10 : len(email_id)]
            if email == "@gmail.com":
                break
            else:
                print("Enter correct email id")
                
        contact_no = int(input("Enter the Phone Number : "))
        
        while True:
            
            print("Note : Enter atleast 8 characters \n")
            password = input("Enter the Password : ")
            if len(password) < 8:
                print("Enter atleast 8 characters\n")
                continue

            print("Re-enter the password")
            print("\n")
            dup_pw = input("Enter the password again : ")


            if password == dup_pw:
                print(signup.signup_details(first_name.upper(), last_name.upper(), email_id.lower(), password, contact_no))
                break
            else:
                print("Password and Repeated password are not the same, Please enter the same for both")




print("Don't have an account?", "\n 1. Create account")
print("Signup")

print("Already have a account", "\n 2. Login")

option = int(input("Enter the option: "))
opt(option)