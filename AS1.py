import sqlite3
import string
import re

def loginScreen(c, conn):
    loggedIn = False
    while loggedIn == False:
        print("Login")
        username = raw_input('What is your Username? Cannot be longer than 8 characters ')
        password = raw_input('What is your Password? Cannot be longer than 30 characters ')
        if re.match("^[A-Za-z0-9_]*$", username) and re.match("^[A-Za-z0-9_]*$", password):
            c.execute("SELECT * FROM staff WHERE login = ? and password = ?;", (username, password))
            row = c.fetchone()
        if row == None:
            options = raw_input("Input S to Sign Up or T to try logging in again! ")
            if options == "S" or options == "s":  
                staff_id = raw_input('What is your Staff ID? Cannot be longer than 5 characters ')
                role = raw_input('What is your role? Enter D for Doctor, N for Nurse or A for Adminstration ')
                name = raw_input('What is your name? Cannot be longer than 15 characters ')
                
                c.execute(" INSERT INTO staff VALUES (?, ?, ?, ?, ?); ", (staff_id, role, name, username, password))
                conn.commit()
                c.execute( ' SELECT login, password FROM staff; ')
                row = c.fetchone()
                print(row)
                
                if len(staff_id) <= 5 and role in ('D', 'N', 'A') and len(name) <= 15 and len(username) <= 8 and len(password) <= 30:
                    loggedIn = True
    return role
                
        
def main():
    import os.path 
    conn = sqlite3.connect('memory')
    c = conn.cursor()
    createTables = open('p1-tables.sql', 'r')
    script = createTables.read()
    c.executescript(script)
    conn.commit()
    createTables.close()
    
    user = loginScreen(c, conn)
    
main()