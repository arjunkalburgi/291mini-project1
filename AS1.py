# CMPUT 291 MINI-PROJECT 1
# 
# Members:
# Mercy Woldmariam
# Andrea Whittaker      1386927

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

# -------------------------- common to doctors and nurses --------------------------

def firstTask():
    
    print("-"*10)
    not_valid = True
    
    # "list all charts in the system ordered by adate"
    c.execute("SELECT * FROM charts ORDER BY adate;")
    
    # "indicating if it is opened or closed"
    # implement . . .
    
    # "the user should be given the option to select a chart"
    while (not_valid):
        
        chartId = input(print("Enter a chart id (0 to quit): "))
        
        if chartId == "0":
            return     
            
        c.execute("SELECT chart_id FROM charts;")
        ids = c.fetchall()
        
        if chartId not in ids:
            print("Invalid chart id. Please try again")
            
        else:
            not_valid = False

    # "all entries associated with that chart must be listed, 
    # ordered by date of entries"
    # implement order. . .
    c.execute('''
    SELECT * 
    FROM charts c, symptoms s, diagnoses d, medications m 
    WHERE c.chart_id=? 
    AND c.chart_id = s.chart_id 
    AND s.chart_id = d.chart_id 
    AND d.chart_id = m.chart_id;
    ''', chartId)

    return

def secondTask(hcno, staff_id):
    
    print("-"*10)
    symptom = input(print("Enter a symptom name: "))
    
    # "add an entry for symptoms"
    c.execute("SELECT hcno, chart_id, staff_id FROM charts, staff")
    #row = 
    # inserts a new row into symptoms -- bulk insert?
    c.executescript('''
    CREATE VIEW update_patient 
    AS SELECT hcno, chart_id, staff_id
    FROM charts, doctors
    WHERE charts.hcno=?
    AND 
    INSERT INTO symptoms VALUES
    ''')
    return

# -------------------------- end common to doctors and nurses --------------------------
# -------------------------- start doctor --------------------------

def getDoctorTask():
    
    not_valid = True
    
    print("-"*10)
    print("Welcome, doctor. Here are the tasks you can perform:")
    
    print("1: List all charts in the system.")
    print("2: Add a symptom to a patient's chart.")
    print("3: Add a diagnosis to a patient's chart.")
    print("4: Add a medication to a patient's chart.")    

    while not_valid:
        
        key = input(print("Enter the number that corresponds to the task (0 to logout): "))
        
        if key not in ('0', '1', '2', '3', '4'):
            print("Invalid input. Please try again.")
        
        else:
            not_valid = False
    
    return key        


def dThirdTask(hcno):
    
    print("-"*10)
    diagnosis = input(print("Enter a diagnosis: "))
    
    # implement . . .
    
    return

def dFourthTask():
    
    return

# -------------------------- end doctor --------------------------
# -------------------------- start nurse --------------------------

def getNurseTasks():
    
    not_valid = True
        
    print("-"*10)
    print("Welcome, nurse. Here are the tasks you can perform:")
    
    print("1: List all charts in the system.")
    print("2: Add a symptom to a patient's chart.")
    print("3: Create a chart for a patient.")
    print("4: Close a patient's chart.")            

    while not_valid:
        
        key = input(print("Enter the number that corresponds to the task (0 to logout): "))
        
        if key not in ('0', '1', '2', '3', '4'):
            print("Invalid input. Please try again.")
        
        else:
            not_valid = False
    
    return key    
    
    
def nThirdTask():
    
    # implement . . .
    
    return

def nFourthTask():
    
    return
    
# -------------------------- end nurse --------------------------
# -------------------------- start admin --------------------------

# -------------------------- end admin --------------------------
# -------------------------- start staff --------------------------
   
def staffLogout():
    
    print("-"*10)
    print("Goodbye!")
    print("-"*10)
    
    return
    
# -------------------------- end staff --------------------------
# -------------------------- start main --------------------------
 
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
    
    # have to implement the rest of the functions . . .
    if user == 'D':
        key = get_doctor_task()
        if key == 1:
            first_task()
        elif key == 2:
            Hcno = input(print("Enter the patient's hcno: "))
            second_task(Hcno)
        elif key == 3:  
            d_third_task()
        elif key == 4:    
            # needs to be made
            d_fourth_task()
        elif key == 0:
            staffLogout()
            loginScreen(c, conn)

    # still have to implement . . .
    elif user == 'N':
        key = get_nurse_task()
        if key == 1:
            first_task()
        elif key == 2:
            Hcno = input(print("Enter the patient's hcno: "))
            second_task(Hcno)
        elif key == 3:  
            n_third_task()
        elif key == 4:    
            n_fourth_task()
        elif key == 0:
            staffLogout()
            loginScreen(c, conn)            

    #implement all functions . . .
    elif user == 'A':
        key = get_admin_task()
        if key == 1:
            a_first_task()
        elif key == 2:
            a_second_task(Hcno)
        elif key == 3:  
            a_third_task()
        elif key == 4:    
            a_fourth_task()
        elif key == 0:
            staffLogout()
            loginScreen(c, conn)              
   

main()