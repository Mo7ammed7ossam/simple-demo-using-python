import register as r
import login as l
import project_functions as pf

DATABASE_PATH = './data_base'
user_file = DATABASE_PATH + "/user.json"

project_file = ""  

def projcet_crud_options():
    
    print("\n", "Select your choice: ")
    print("\t" * 2, "1- View all projects")
    print("\t" * 2, "2- Create a project")
    print("\t" * 2, "3- Edit a project")
    print("\t" * 2, "4- Delete a project")
    print("\t" * 2, "5- Back")
    
    choice = input("")

    if choice.isdigit() and int(choice) in [1, 2, 3, 4, 5]:
        if int(choice) == 1:
            pf.Project.print_all_projects(project_file)
            
        elif int(choice) == 2:
            pf.Project.create_project(project_file)
            
        elif int(choice) == 3:
            pf.Project.edit_project(project_file)
            
        elif int(choice) == 4:
            pf.Project.delete_project(project_file)
            
        elif int(choice) == 5:
            home_page_actions()

        print("\n")
        projcet_crud_options()
    else:
        print("\n-------------------- Enter valid choice !!! -------------------------\n")
        home_page_actions()
#---------------------------------------------------------------#

def create_projects_file(email):
    global project_file
    project_file =  DATABASE_PATH + "/" + email + ".json"
#---------------------------------------------------------------#

def user_login():
    print('''
                                    -------------------------------------------------------------------
                                    -                          Log in Page                            -
                                    -------------------------------------------------------------------
    ''')
    
    email = input("Enter you email : ")
    password = input("Enter you password : ")
    
    if l.login(user_file, email, password): #if true
        
        #create file for projects for this user
        create_projects_file(email)
        projcet_crud_options()
    else:
        print("------------------ Wrong credentials !!! ---------------------")
        home_page_actions()
#---------------------------------------------------------------#

def home_page_actions():
    print("Please select your choice : ")
    print("\t" * 2, "1- Register")
    print("\t" * 2, "2- login")
    choice = input("")
    
    if choice.isdigit() and int(choice) in [1, 2]:
        
        if int(choice) == 1:
            r.register(user_file)
            
            #redirect to home page
            home_page_actions()
        elif int(choice) == 2:
            user_login()
    else:
        print("\n")
        print("Enter valid choice !!!")
        home_page_actions()
#---------------------------------------------------------------#

#---------------------------------------------------------------#
#----------------------- start from here -----------------------#
#---------------------------------------------------------------#

print('''
                            -------------------------------------------------------------------
                            -                           Home Page                             -
                            -------------------------------------------------------------------
''')

home_page_actions()    