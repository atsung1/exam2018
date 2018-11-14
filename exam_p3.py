class Employee:
    """
    the base class
    """
    nextIDNum = 0
    def __init__(self, name):
        self.name = name
        self.idNum = Employee.nextIDNum
        Employee.nextIDNum += 1

    def __str__(self):
        return 'Employee Name:{}    Employee ID:{}'.format(self.name, self.idNum)

    def get_name(self):
        return self.name

    def weekly_pay(self, hours_worked):
        return 0


class Nonexempt_Employee(Employee):

    def __init__(self, name, hourly_rate):
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate

    # Overrides the superclass method.
    def weekly_pay(self, hours_worked):
        #<= 40, 1X; >40 hours, 1.5X
        pay = 0
        if hours_worked <= 40:
            pay += hours_worked*self.hourly_rate
        else:
            pay += (hours_worked//40)*40*self.hourly_rate
            pay += (hours_worked%40)*self.hourly_rate*1.5
        return pay

class Exempt_Employee(Employee):

    def __init__(self, name, annual_salary):
        Employee.__init__(self, name)
        self.annual_salary = annual_salary

    def weekly_pay(self, hours_worked):
        hours_worked = self.annual_salary/52
        return hours_worked


class Manager(Exempt_Employee):

    def __init__(self, name, annual_salary, bonus):
        Exempt_Employee.__init__(self, name, annual_salary)
        self.bonus = bonus

    def weekly_pay(self, hours_worked):
        hours_worked = (self.annual_salary+self.bonus)/52
        return hours_worked

def main():
    all_employees = []
    all_employees.append(Nonexempt_Employee("Aaron Wendell", 40.0))
    all_employees.append(Exempt_Employee("Alden Pexton", 60000.0))
    all_employees.append(Manager("Allison Fernandez", 94000.0, 50.0))

    for employee in all_employees:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Salary: ", pay)
    # cyn = Employee('Cynthia Yong')
    # print(cyn)
    # print(cyn.get_name())
    # ang = Employee('Angela Tsung')
    # print(ang)
    # print(ang.get_name())
    # kit = Nonexempt_Employee('Kit Tan', 50)
    # print(kit)
    # print(kit.weekly_pay(50))

if __name__ == '__main__':
    main()
