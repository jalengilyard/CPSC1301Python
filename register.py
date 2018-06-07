## Cash register side project

class Register:
    def __init__(self):
        self.sales = 0
        self.employees_OTC = 0

    employees = {
            "Jalen": {
                "Name": "Jalen",
                "Job": "OEmd",
                "Password": 1022
                },
            "Cashier": {
                "Name": "Cashier",
                "Job": "Cashier",
                "Password": 999
                },
            "Manager": {
                "Name": "Manager",
                "Job": "Manager",
                "Password": 903039
                }
        }

    
    def employee_clock_in(self, login, password):
        for x in self.employees:
           if self.employees[x]["Name"] == login and self.employees[x]["Password"] == password:
               print("You are now clocked in: %s, %s" % (self.employees[x]["Name"], self.employees[x]["Job"]))
               self.employees_OTC += 1

    def employee_clock_out(self, login, password):
        for x in self.employees:
            if self.employees[x]["Name"] == login and self.employees[x]["Password"] == password:
                print("You are now clocked out: %s, %s" % (self.employees[x]["Name"], self.employees[x]["Password"]))
                self.employees_OTC -= 1
user = Register()
logon = input("Enter your logon: ")
password = int(input("Enter your password: "))
user.employee_clock_in(logon, password)
print(user.employees_OTC)

def main():


main()
