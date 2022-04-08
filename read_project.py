import validation as v

class Projcect_Data:
    
    @classmethod
    def read_project_details():
        details = input("Enter project details : ")
        return details
    #-----------------------------------------------------------------#

    @classmethod
    def read_project_total_target(self):
        total_target = input("Enter total target : ")
        
        #validate if only digits
        if not total_target.isdigit():
            print("\n------------------ Enter valid total target !!! -------------------\n")
            
            return self.read_project_total_target()
        return total_target
    #-----------------------------------------------------------------#

    @classmethod
    def read_project_start_date(self):
        date = input("Enter start date : ")
        
        #validate date
        if not v.Validation.is_valid_date(date):
            print("\n--------------- Enter valid start date !!! ----------------------\n")
            
            return self.read_project_start_date()
        return date
    #-----------------------------------------------------------------#

    @classmethod
    def read_project_end_date(self):
        date = input("Enter end date : ")
        
        #validate date
        if not v.Validation.is_valid_date(date):
            print("\n------------------------- Enter valid end date !!! -------------------------\n")
            
            return self.read_project_end_date()
        return date
    #-----------------------------------------------------------------#
