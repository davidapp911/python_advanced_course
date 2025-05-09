import enum
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List

# abstract class
@dataclass
class Employee(ABC):
    # attributes of abstract class Employee
    name: str
    emp_id: str = field(default=None, init=False)
    _company: 'Company' = field(default=None, init=False)

    _last_assigned_id = 0 # class-level attribute

    # getter setter methods
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company):
        self._company = company

    # auto generates employee id number
    def __post_init__(self):
        Employee._last_assigned_id += 1
        self.emp_id = f"E{Employee._last_assigned_id}"

    # method to be implemented by children classes
    @abstractmethod
    def calculate_payment(self) -> float:
        pass

    # method when employee leaves a company
    def leave_company(self) -> None:
        if self.company is not None:
            return self.company.fire(self)

        raise ValueError("Employee doesn't work at any company")

# subclass to define hour rate employee
@dataclass
class HourlyEmployee(Employee):
    _hourly_rate: float = field(default=0, init=False) # hourly rate the employee gets paid

    # getter setter methods
    @property
    def hourly_rate(self) -> float:
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, rate: float):
        self._hourly_rate = rate

    def calculate_payment(self) -> float: # calculates employee payment assuming a 40 hour week for 1 week
        return round(self.hourly_rate * 40, 2)

# subclass to define salaried employee
@dataclass
class SalariedEmployee(Employee):
    _salary: float = field(default=0, init=False) # monthly salary of employee

    # getter setter methods
    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, salary: float):
        self._salary = salary

    def calculate_payment(self) -> float: # calculates employee payment by dividing monthly salary over 4 weeks
        return round(self.salary/4, 2)

# company domain class
class Domain(enum.Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    RETAIL = "Retail"

# company class
@dataclass
class Company:
    # company attributes
    name: str
    domain: Domain
    employees: List[Employee] = field(default_factory=list)

    def __repr__(self): # company objectprint
        return f"Company({self.name}, {self.domain.name}, Employees={len(self.employees)})"

    def hire(self, employee: Employee) -> None: # company hires employee of it doesn't have a company
        if employee.company is None:
            employee.company = self
            return self.employees.append(employee)

        raise ValueError(f"{employee.name} cannot be hired. He already works at {employee.company.name}")

    def fire (self, employee: Employee) -> None: # company fires employee if employee is in its employees lists
        if employee in self.employees:
            employee.company = None
            return self.employees.remove(employee)

        raise ValueError(f"{employee.name} is not part of {self.name}.")

    def raise_pay(self, employee: Employee, extra_rate: float): # raises the salary of employee by extra_rate if employee in employees list
        if employee not in self.employees:
            raise ValueError(f"{employee.name} is not part of {self.name}.")

        if isinstance(employee, HourlyEmployee):
            employee.hourly_rate += extra_rate
        if isinstance(employee, SalariedEmployee):
            employee.salary += extra_rate


def main():
    # generate companies
    tech_company = Company(name="NeuroSpark Technologies", domain=Domain.TECHNOLOGY)
    health_company = Company(name="Vitalis Health Group", domain=Domain.HEALTHCARE)

    # generate some employees
    Bruno = HourlyEmployee(name="Bruno")
    David = SalariedEmployee(name="David")
    Mark = HourlyEmployee(name="Mark")
    John = SalariedEmployee(name="John")

    # companies hire employees
    health_company.hire(Bruno)
    health_company.hire(David)
    tech_company.hire(Mark)
    tech_company.hire(John)

    print(tech_company)
    print(health_company)

    # check that company only hires employees that dont belong to a company
    try:
        health_company.hire(David)
    except ValueError as e:
        print(e)

    # test firig function
    tech_company.fire(Mark)
    print(tech_company.employees)
    health_company.fire(David)
    print(health_company.employees)

    # check that companies cannot fire employees that are not part of the company
    try:
        health_company.fire(David)
    except ValueError as e:
        print(e)


    # set and test payment raise function
    Bruno.hourly_rate = 46.27
    John.salary = 7590.13
    print(health_company.employees)
    print(tech_company.employees)
    print(Bruno.calculate_payment())
    print(John.calculate_payment())

    health_company.raise_pay(Bruno, 10.0)
    print(Bruno.calculate_payment())
    print(health_company.employees)

    # check that a company cannot raise the salary of an employee from a different company
    try:
        tech_company.raise_pay(Bruno, 10.0)
    except ValueError as e:
        print(e)

    # check that employees can leave their company
    John.leave_company()
    print(tech_company)
    print(health_company)


if __name__ == "__main__":
    main()