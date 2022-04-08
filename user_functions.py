import json
import file_functions as ff

class User:
    def get_all_users(user_file):
        if ff.is_file_empty(user_file):
            return []
        else:
            file = None
            try:
                file = open(user_file, "r")
                
                # convert from json obj to dictionary
                return json.load(file)
            except Exception as e:
                print("Exception: ", e)
            finally:
                if file is not None:
                    file.close()
    #---------------------------------------------------------#

    @classmethod
    def create_new_user(self, user_file, user_data):
        all_users = self.get_all_users(user_file)

        file = None
        try:
            file = open(user_file, "w")
            
            all_users.append(user_data)
            
            # dumps --> convert from dictionary to json obj
            file.write(json.dumps(all_users))
            
            print('\n-------------- new user added successfully ----------------\n')
                
        except Exception as e:
            print("Exception: ", e)
        finally:
            
            if file is not None:
                file.close()
    #---------------------------------------------------------#

