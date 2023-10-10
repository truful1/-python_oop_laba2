class Employee:
    pass

employee1 = Employee()
employee1.name = 'John'
employee1.salary = 5000

employee2 = Employee()
employee2.name = 'Anna'
employee2.salary = 6000

employee3 = Employee()
employee3.name = 'Mike'
employee3.salary = 4500

total_salary = employee1.salary + employee2.salary + employee3.salary
print("Сумма зарплат работников:", total_salary)