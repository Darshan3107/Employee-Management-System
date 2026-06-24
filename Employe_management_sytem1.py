class Employe_management_sytem:
    def __init__(self):
        self.emp = {}
        #add employe it is new method
    def add_employe(self):
        n = int(input("enter a number u want to add employes:"))
        for i in range(n):
            print(f"==========================={i+1}======================")
            empid = int(input(f"enter {i+1} employe ID: "))
            while empid in self.emp:
                print("Employee ID already exists. Enter a unique ID.")
                empid = int(input(f"Enter {i+1} Employee ID again: "))
            name = input(f"Enter a {i+1} Employe Name:")
            age = int(input(f"Enter a {i+1} employe age:"))
            department = input(f"enter {i+1} employe department:")
            salary = float(input(f"Enter a {i+1} employesalry:"))
            employes =  {empid: {'name': name, 'age': age, 'department': department, 'salary': salary}}
            self.emp.update(employes)
            print("employee was successfully added...")
    def view_all_employes(self):
        if len(self.emp)>0:
            print("ID\t\tName\t\t Age\t\tDepartment\t\tSalary")
            for key, value in self.emp.items():
                     print(f"{key}\t\t{value['name']}\t\t{value['age']}\t\t{value['department']}\t\t{value['salary']}")
        else:
                print("No employees available.")
    def  Search_Employee(self):
        search_empid = int(input("enter u want to search ID:"))
        if search_empid in self.emp:
            value = self.emp[search_empid]
            print("Name\t\t Age\t\tDepartment\t\tSalary")
            print(f"{value['name']}\t\t{value['age']}\t\t{value['department']}\t\t{value['salary']}")
        else:
             print("Employee not found.")
    def main_menu(self):
        while(True):
              print("Enter choice 1 is for add employe:")
              print("Enter choice 2 is for view all employes information:")
              print("Enter choice 3 is search the employe:")
              print("Enter choice 4 for exit the program:")
              choice = int(input("enter a choice:"))
              match(choice):
                    case 1:
                        self.add_employe()
                    case 2:
                        self.view_all_employes()
                    case 3:
                        self.Search_Employee()
                    case 4:
                        print("Thx for using this program ")
                        break
                    case _:
                        print("Ur Selection of Operations is wrong!!")     
e1 = Employe_management_sytem()
e1.main_menu()