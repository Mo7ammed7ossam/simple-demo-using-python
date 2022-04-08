import json
import read_project as rp
import file_functions as ff



class Project:
    
    DATABASE_PATH = './data_base'

    def get_all_projects_list(project_file):
        if ff.is_file_empty(project_file):
            return []
        else:
            file = None
            try:
                file = open(project_file, "r")
                return json.loads(file.read())
            except Exception as e:
                print("Exception: ", e)
            finally:
                if file is not None:
                    file.close()
    #-----------------------------------------------------------#                

    @classmethod
    def is_project_exists(self, project_file, project_title):
        all_projects = self.get_all_projects_list(project_file)
        
        if len(all_projects) == 0:
            return False
        
        for project in all_projects:
            if project["title"] == project_title:
                return True
        return False
    #-----------------------------------------------------------#                

    @classmethod
    def print_all_projects(self, project_file):
        all_projects = self.get_all_projects_list(project_file)
        
        if len(all_projects) == 0:
            print("\n--------------- No projects found !!! -----------------\n")
            return
        for project in all_projects:
            print('\n')
            print(project)
    #-----------------------------------------------------------#                


    #crud on projects
    @classmethod
    def create_project(self, project_file):
        title = input("Enter project Title : ")

        if self.is_project_exists(project_file, title):
            print("\n---------------- Project exists !!! ----------------\n")
            return

        details = rp.Projcect_Data.read_project_details()
        total_target = rp.Projcect_Data.read_project_total_target()
        start_date = rp.Projcect_Data.read_project_start_date()
        end_date = rp.Projcect_Data.read_project_end_date()
        
        project = {
            "title": title,
            "details": details,
            "total_target": total_target,
            "start_date": start_date,
            "end_date": end_date,
        }

        all_projects = self.get_all_projects_list(project_file)
        all_projects.append(project)
        
        print('\n------------------ project created successfully ----------------\n')

        file = None
        try:
            file = open(project_file, "w")
            file.write(json.dumps(all_projects))
        except Exception as e:
            print("Exception: ", e)
        finally:
            if file is not None:
                file.close()
    #-----------------------------------------------------------#                

    @classmethod
    def edit_project(self, project_file):
        project_title = input("Enter project title : ")

        if not self.is_project_exists(project_file, project_title):
            print("Project not exists!")
            return

        all_projects = self.get_all_projects_list(project_file)
        
        for project in all_projects:
            if project["title"] == project_title:
                
                print("project Deatials : {} \n".format(project['details']))
                select = input("Edit details ? [yes/no]")
                if select == "yes":
                    project["details"] = input("Enter project's new details : ")
                
                print("project total_target : {} \n".format(project['total_target']))
                select = input("Edit total_target ? [yes/no]")
                if select == "yes":
                    project["total_target"] = input("Enter project's new total_target : ")
                    
                print("project start_date : {} \n".format(project['start_date']))
                select = input("Edit start_date ? [yes/no]")
                if select == "yes":
                    project["start_date"] = input("Enter project's new start_date : ")
                    
                print("project end_date : {} \n".format(project['end_date']))
                select = input("Edit end_date ? [yes/no]")
                if select == "yes":
                    project["end_date"] = input("Enter project's new end_date : ")

                file = None
                try:
                    file = open(project_file, "w")
                    file.write(json.dumps(all_projects))
                except Exception as e:
                    print("Exception: ", e)
                finally:
                    if file is not None:
                        file.close()
                break
    #-----------------------------------------------------------#                

    @classmethod
    def delete_project(self, project_file):
        project_title = input("Enter project title : ")

        if not self.is_project_exists(project_file, project_title):
            print("Project not exists!")
            return

        all_projects = self.get_all_projects_list(project_file)
        
        for project in all_projects:
            if project["title"] == project_title:
                all_projects.remove(project)
            
                print('\n------------------ project deleted successfully ----------------\n')

                file = None
                try:
                    file = open(project_file, "w")
                    file.write(json.dumps(all_projects))
                except Exception as e:
                    print("Exception: ", e)
                finally:
                    if file is not None:
                        file.close()
                break
    #-----------------------------------------------------------#