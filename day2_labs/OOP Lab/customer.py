from person import Person

class Customer(Person):

    def __init__(self,
                 first_name,
                 last_name,
                 account_number):
        super(Customer,self).__init__(first_name, last_name)
        self._account_number = account_number

    def getAccountNumber(self):
        return self._account_number

    def isCustomer(self):
        return True