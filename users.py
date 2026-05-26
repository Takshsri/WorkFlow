class User:
    def __init__(self,user_id,name,role,password):
        self.id = user_id
        self.name = name
        self.role = role
        self.password = password
    
    def display_user_info(self):
        print(f"User ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Password: {self.password}")


              
