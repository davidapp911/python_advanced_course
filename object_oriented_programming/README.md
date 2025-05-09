# Task Instructions
In this task, you will be creating a system to manage a company's employees. The company has both salaried and hourly employees. 


The aim of this task is to practice object-oriented programming in Python, including the use of dataclasses, inheritance, and abstract base classes. It will also involve using Python's built-in data types, control structures, and functions.

In this task, you will be creating a system to manage a company's employees.
The company has both salaried and hourly employees. The aim of this task is to
practice object-oriented programming in Python, including the use of
dataclasses, inheritance, and abstract base classes. It will also involve using
Python's built-in data types, control structures, and functions.

1. Employee Class
- Define an abstract base class Employee (inheriting from ABC) using
dataclasses. (Import ABC and abstractmethod from the abc module.)
- Attributes
  - name(str) - The name of the employee.
  - emp_id(str) - Default None. The unique identifier for employee.
  This is automatically generated in the __post_init__ method.
  Format : “E1”, “E2”…,“En”.
  - _company(Default None - This is protected and can be accessed
  and modified with the company property and setter.).
  - _last_assigned_id: This is a class-level attribute used to generate
  unique employee IDs.
- Add an abstract method calculate_payment in the Employee class (will
  be implemented in the subclasses).
2. HourlyEmployee Class
- Create a subclass of Employee named HourlyEmployee. It should have
an additional attribute
_hourly_rate(int).
- Add setters and getters for _hourly_rate
- Implement the calculate_payment method in HourlyEmployee. Assume
it a 40-hour work week. Calculate for one week.
3. SalariedEmployee Class
- Create a subclass of Employee named SalariedEmployee. It should have
an additional attribute
_salary(int). (for one month)
- Add setters and getters for salary.
- Implement the calculate_payment method in SalariedEmployee.
Calculate for one week.
4. Company class
- Add class named Domain and make sure it inherits from the
Enum(enum.Enum) class. Within this class, define three class variables:
TECHNOLOGY, HEALTHCARE, and RETAIL. Assign each of them a
string value that matches their variable name.
- Create using dataclasses Company class with attributes name(int),
domain (Domain), employees (list).
- Implement a hire method that takes an employee object and adds it to the
employees list. (without duplication). Employee can’t work in 2
companies at time.
- Implement a fire method that takes an employee and removes from the
employees list.
- Implement a raise_pay method that takes an employee object and an
amount. This method should increase the salary of a SalariedEmployee
or the hourly rate of an HourlyEmployee by the specified amount.
- Implement the __repr__ method. The string representation should be in
the format "Company(name, domain.name, Employees:
number_of_employees)"
.
6. Implement a leave_company method in the Employee class. The method
should check if the employee is currently employed by a company. If yes, the
method should call the fire method of the company to remove the employee
from the company's list of employees. If not - a message saying that the
employee is not currently employed by any company.
7. Add a script that tests various functionalities of the program and check:
- Create 2 companies with different domains.
- Create few various types of employees.
- Hire of various types of employees (hire method).
- Verify that employees are added to the company's list of employees,
emp_id aren’t duplicated.
- Attempting to hire the same employee twice.
- Remove employees from the company using the fire method. Verify that
employees are no longer in the company's list of employees.
- Attempting to fire an employee not employed by the company. Verify that
attempting to fire an employee not employed by the company doesn't
affect the employee list.
- Set and get salaries/hourly_
rates for various employees;
- Call the calculate_payment method and verify that the payment is
calculated correctly.
- Increase the salary or hourly_
rate of an employee using the raise_pay
method.
- Attempting to raise
_pay for an employee not employed by the company.
- For an employee currently employed by a company, call the
leave_company method.
- Call the __repr__ method of the Company class and verify that it returns
a string representation in the correct format.