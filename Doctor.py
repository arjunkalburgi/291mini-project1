from Staff import staff
from Main import c          # if we use separate files, would have to import c (too complex?)
import sqlite3

class doctor(staff):
    
    '''
    Gives the doctor a list of options, and calls a function
    to perform the specified task. Goes to the logout screen
    when the user is finished.
    '''
    def get_doctor_task(self):
    
        print("Welcome, doctor. Here are the tasks you can perform:")
        
        print("-"*10)
        print("1: List all charts in the system.")
        print("2: Add a symptom to a patient's chart.")
        print("3: Add a diagnosis to a patient's chart.")
        print("4: Add a medication to a patient's chart.")
        key = int(input(print("Enter the number that corresponds to the task (0 to logout): ")))
        return key        
        
        ''' start section: this code can go in main or the login thing maybe '''
        #if key == 1:
                #    first_task()

                #elif key == 2:
                #    Hcno = input(print("Enter the patient's hcno: "))
                #    second_task(Hcno)

                #elif key == 3:
                    # call function

                #elif key == 4:
                    # call function

                #elif key == 0:
                    # call function that logs the user out        
        ''' end section '''
               
    '''
    Performs the first task using an SQL query
    '''
    def first_task(self):
        
        c.execute("SELECT * FROM charts ORDER BY adate;")
        chartId = input(print("Enter a chart id (0 to quit): "))
        
        if chartId == "0":
            return
        
        c.execute('''
        SELECT * 
        FROM charts c, symptoms s, diagnoses d, medications m 
        WHERE c.chart_id=? 
        AND c.chart_id = s.chart_id 
        AND s.chart_id = d.chart_id 
        AND d.chart_id = m.chart_id;
        ''', chartId)
        
        return
    
    def second_task(self, Hcno):
        
        symptom = input(print("Enter a symptom name: "))
        
        # inserts a new row into symptoms
        c.execute('''
        INSERT INTO symptoms VALUES
        ''')
        return
