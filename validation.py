import re
from datetime import datetime

# user data validation

class Validation:

    def name_validation(name):
        return re.search("^[a-zA-Z]+$", name)
    #---------------------------------------------------#

    def email_validation(email):
        return re.search(r"^[\w.+\-]+@[\w]+\.[a-z]+$", email)
    #---------------------------------------------------#

    def password_confirmation_validation(passwd, passwd_confirmation):
        if len(passwd) < 8:
            return False
        else:
            return passwd == passwd_confirmation
    #---------------------------------------------------#

    def phone_number_validation(phone):
        # validate these numbers only
        return re.search(r"^(010|011|012|015)[0-9]{8}$", phone)
    #---------------------------------------------------#

    # projrct data validation

    def validate_date(date):
        try:
            datetime.strptime(date, "%d-%m-%Y")
            return True
        except ValueError:
            return False
    #-------------------------------------------------------------------------------#

    @classmethod
    def is_valid_date(self, date):
        if not self.validate_date(date):
            return False
        if datetime.strptime(date, "%d-%m-%Y") > datetime.now():
            return False
        return True
    #-------------------------------------------------------------------------------#













