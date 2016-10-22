#create a new staff member
def new_staff(staff_id, role, name, login, password):
    
    insertion = ([staff_id, role, name, login, password])
    c.execute("INSERT INTO staff VALUES (?)", insertion)

# logs the user out of the system, returns to the login screen    
def staff_logout():
    
    print("Goodbye!")
    print("-"*10)
    
    return
    # call the login function in main
    
def get_nurse_tasks():
    print("Welcome, nurse. Here are the tasks you can perform:")
    print("-"*10)
    print("1: List all charts in the system.")
    print("2: Add a symptom to a patient's chart.")
    print("3: Create a chart for a patient.")
    print("4: Close a patient's chart.")
    key = int(input(print("Enter the number that corresponds to the task (0 to logout): ")))    
    print("-"*10)
    
def n_third_task():
    
