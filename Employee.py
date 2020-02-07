class Employee():
    employeeCount =0
    salary =0
    def __init__(self,pname,pfamily,psalary,pdepartment):
        self.name=pname
        self.family=pfamily
        Employee.salary+=psalary
        self.department=pdepartment
        Employee.employeeCount=Employee.employeeCount+1
    def printAllEmployees(self):
        print('Name: '+self.name+' Family: '+self.family+' Department: '+self.department)

    def averageSalary(self):
        self.avgSalary=Employee.salary/Employee.employeeCount
        print ('The average salary of the employees is')
        print (self.avgSalary)

class FullTimeEmployee(Employee):
    def __init__(self):
        Employee.averageSalary(self)



e1=Employee('Nikhitha','Kolluri',2000,'Software Engineer')
e1.printAllEmployees()

e2=Employee('Bhuna','Inakollu',3000,'Software Engineer')
e2.printAllEmployees()

e3=Employee('Ruchitha','Bathula',1000,'Software Engineer')
e3.printAllEmployees()

f=FullTimeEmployee()