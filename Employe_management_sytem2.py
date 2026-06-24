class Employe_management_sytem:
    def __init__(self):
        self.emp = []
    def add_employe(self):
        n = int(input("enter a number u want to add employes:"))
        for i in range(n):
            print(f"==========================={i+1}======================")
            empid = int(input(f"enter {i+1} employe ID: "))
            if(empid in self.emp):
                print("Enter a unique code this id is already exist")
            else:
                    name = input(f"Enter a {i+1} Employe Name:")
                    age = int(input(f"Enter a {i+1} employe age:"))
                    department = input(f"enter {i+1} employe department:")
                    salary = float(input(f"Enter a {i+1} employesalry:"))
                    employes =  {empid: {'name': name, 'age': age, 'department': department, 'salary': salary}}
                    self.emp.append(employes)
                    print("employee was successfully added...")
        if len(self.emp)>0:
            print("ID\t\tName\t\t Age\t\tDepartment\t\tSalary")
            for i in self.emp:
                for key, value in i.items():
                    print(key,"\t",value['name'],"\t",value['age'],"\t",value['department'],"\t",value['salary'])
        else:
            print("No employees available.")
    def search_for_employee(self):
         search_employe = input("enter you want search employee:")
         if search_employe in self.emp:
              print("you are searched employes information: ",self.empid)
         else:
              print("invalid")
    def menu_system(self):
        while(True):
            print("Enter choice 1 for add_employe..")
            print("Enter choice 2 for view_all_employes..")
            print("Enter choice 3 for search_for_employe..")
            print("enter choice 4 for exit the program..")
            choice = int(input("enter a choice:"))
            if(choice ==1):
                self.add_employe()
            elif(choice == 2):
                self.view_all_Employees()
            elif(choice == 3):
                self.search_for_employee()
            else:
                print("exited to program...")
                break
E1 = Employe_management_sytem()
E1.menu_system()
