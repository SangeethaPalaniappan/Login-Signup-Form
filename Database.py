# Database

import sqlite3

class Database:
    def add_details(self, f_name, l_name, email_id, password, contact_no):
        con = sqlite3.connect('UserDetails.db')
        cursor = con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS UserDetails
                        (id INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, Emailid VARCHAR, Password VARCHAR, ContactNo INTEGER)''')

        if self.existing_check(email_id, "signup") == 1:

            cursor.execute("INSERT INTO UserDetails (FirstName, LastName, Emailid, Password, ContactNo) VALUES (?, ?, ?, ?, ?)", (f_name, l_name, email_id, password, contact_no))
            con.commit()


        else:
            return 0  

        con.close()
        return 1

    def fetch_details(self, email_id, type):
        con = sqlite3.connect('UserDetails.db')
        cursor = con.cursor()
        cursor.execute("SELECT Emailid, Password FROM UserDetails WHERE Emailid = ?", (email_id,))
        
        details = cursor.fetchone()
        if details != None:
            mail = details[0]
            pw = details[1]
            if type == "login":
                return mail, pw
                
                
            elif type == "signup":
                return mail, pw 
        else:
            return 1, 1    

    def authenticate(self, email_id, password):
        mail, pw = self.fetch_details(email_id, "login", password)
        if email_id == mail and password == pw:
            return 1
        return 0

    def existing_check(self, email_id, mail):
        mail, pw = self.fetch_details(email_id, "signup")
        if email_id == mail:
            return 0
        return 1  
