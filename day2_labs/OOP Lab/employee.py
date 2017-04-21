from person import Person

class Employee(Person):

    def __init__(self,
                 first_name,
                 last_name,
                 job_title,
                 gender,
                 salary):
        super(Employee, self).__init__(first_name, last_name)
        self._jobtitle = job_title
        self._gender = gender
        self._salary = salary

    def getSalary(self):
        return self._salary

    def getGender(self):
        return self._gender

    def getJobTitle(self):
        return self._jobtitle

    def isEmployee(self):
        return True