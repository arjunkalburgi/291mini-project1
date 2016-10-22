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
    print("4: Add a medication to a patient's chart."
    key = int(input(print("Enter the number that corresponds to the task (0 to logout): ")))
    return key        

    ''' start section: this code can go in main or the login thing maybe '''
    #if key == 1:
    #    first_task()

    #elif key == 2:
    #    Hcno = input(print("Enter the patient's hcno: "))
    #    second_task(Hcno)
    #elif key == 3:  
    #    call function
    #elif key == 4:    
    #    call function
    #elif key == 0:
    #    call function that logs the user out        
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

def second_task(hcno, staff_id):
    
    # should we ask for their staff_id?
    symptom = input(print("Enter a symptom name: "))
    
    c.execute("SELECT hcno, chart_id, staff_id FROM charts, staff")
    row = 
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

def d_third_task(hcno):
    
    diagnosis = input(print("Enter a diagnosis: "))
    
    
