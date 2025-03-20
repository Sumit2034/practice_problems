class User:

    def __init__(self, user_id, user_name, email, mobile_number):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.mobile_number = mobile_number
        
    
    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name
    
    def get_email(self):
        return self.email

    def get_mobile_number(self):
        return self.mobile_number