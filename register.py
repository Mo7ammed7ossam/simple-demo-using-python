import read_data as rd
import user_functions as uf


def register(file):

    print('''
                            -------------------------------------------------------------------
                            -                    Registeration Page                           -
                            -------------------------------------------------------------------
    ''')

    first_name = rd.User_Data.read_first_name()
    last_name = rd.User_Data.read_last_name()
    email = rd.User_Data.read_email()
    password = rd.User_Data.read_password()
    phone_number = rd.User_Data.read_phone_number()
    
    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone_number": phone_number
    }
    
    uf.User.create_new_user(file, user_data)
#----------------------------------------------------------------------------------#


