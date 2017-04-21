from employee import Employee
from customer import Customer

class MainClass():

    def registerEmployee(self,
                         first_name,
                         last_name,
                         job_title,
                         gender,
                         salary):
        employee = Employee(
            first_name,
            last_name,
            job_title,
            gender,
            salary
        )
        return employee

    def registerCustomer(self,
                         first_name,
                         last_name,
                         account_number):
        customer = Customer(
            first_name,
            last_name,
            account_number
        )
        return customer

if __name__ == '__main__':
    start = MainClass()
    employee = start.registerEmployee(
        'Baker',
        'Sekitoleko',
        'Developer',
        'Male',
        300000
    )
    customer = start.registerCustomer(
        'Henry',
        'Bulemi',
        'CU001'
    )
    print(
        employee.getName(),
        employee.getSalary(),
        employee.getJobTitle(),
        employee.getGender(),
        employee.isEmployee()
    )
    print(
        customer.getName(),
        customer.getAccountNumber(),
        customer.isCustomer()
    )