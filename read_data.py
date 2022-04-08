import validation as v

class User_Data:
    @classmethod
    def read_first_name(self):
        first_name = input("Enter your first name : ")
        
        #validate name
        if not v.Validation.name_validation(first_name):
            print("Enter valid first name !!!")
            
            #call function again
            return self.read_first_name()
        return first_name
    #------------------------------------------------------------------#

    @classmethod
    def read_last_name(self):
        last_name = input("Enter your last name : ")
        
        #validate name
        if not v.Validation.name_validation (last_name):
            print("Enter valid last name !!!")
        
            #call function again
            return self.read_last_name()
        return last_name
    #------------------------------------------------------------------#
    
    @classmethod
    def read_email(self):
        user_email = input("Enter your email : ")
        
        #validate email
        if not v.Validation.email_validation(user_email):
            print("Enter valid email !!!")
            
            #call fun again
            return self.read_email()
        return user_email
    #------------------------------------------------------------------#
    
    @classmethod
    def read_password(self):
        user_password = input("Enter your password : ")
        confirm_password = input("Confirm your password : ")
        
        #validate password
        if not v.Validation.password_confirmation_validation(user_password, confirm_password):
            print("Enter valid password! [at least 8 chars]")
            
            #call fun again
            return self.read_password()
        return user_password
    #------------------------------------------------------------------#
    
    @classmethod
    def read_phone_number(self):
        phone_number = input("Enter your phone number : ")
        
        if not v.Validation.phone_number_validation(phone_number):
            print("Enter valid phone_number!")
            
            return self.read_phone_number()
        return phone_number
    #------------------------------------------------------------------#
