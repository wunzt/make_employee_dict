# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/17/2022
# Description: Takes

class Employee:
    """Represents an employee with a name, ID, salary, and email."""

    def __init__(self, name, ID_number, salary, email_address):
        """Creates an employee object with a name, ID, salary, and email."""

        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """Returns the name."""
        return self._name

    def get_ID_number(self):
        """Returns the ID number."""
        return self._ID_number

    def get_salary(self):
        """Returns the salary."""
        return self._salary

    def get_email_address(self):
        """Returns the email address."""
        return self._email_address

def make_employee_dict(name, ids, salary, email):
    """Creates a dictionary entry for each employee with their ID number as the key."""

    Emp_Dict = {}

    i = 0

    while i < len(name):

        Emp_Dict[ids[i]] = Employee(name[i], ids[i], salary[i], email[i])

        i += 1

    return Emp_Dict