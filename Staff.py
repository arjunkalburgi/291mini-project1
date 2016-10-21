import Main

class staff:
    
    def __init__(self, staff_id_, role_, name_, login_):
        
        self.staff_id = staff_id_
        self.role = role_
        self.name = name_
        self.login = login_
    
    # logs the user out of the system, returns to the login screen    
    def staff_logout(self):
        
        print("Goodbye!")
        print("-"*10)
        
        return
        # call the login function in main