import user_functions as uf
import file_functions as ff





def login(user_file, email, password):
    
    if ff.is_file_empty(user_file): # if empty
        return False
    else:
        all_users = uf.User.get_all_users(user_file)
        
        for user in all_users:
            if user["email"] == email and user["password"] == password:
                print("\n---------------- user LoggedIn -------------------\n")
                return True
        return False
#------------------------------------------------------------------#