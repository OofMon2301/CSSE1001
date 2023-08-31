from __future__ import annotations


class Employee(object):
    """
    A salaried employee.

    """

    def __init__(self, name: str, salary: float) -> None:
        """
        Initialise a new Employee instance.

        Parameters:
            name (str): The employee's name.
            salary (float): The employee's annual salary.
        """
        super().__init__()
        self._name = name
        self._salary = salary
        self._bonus = 0
        # Call Executive.wage from Employee.wage (using super) to get the correct result.

    def get_name(self) -> str:
        """
        (str) Return the name.
        """

        return self._name

    def wage(self) -> float:
        """
        (float) Return the forgnightly wage.
        """
        # Call Employee.wage from Executive.wage (using super) to get the correct result.
        return self._salary / 26


# Define a subclass of Employee called Worker. A worker has a manager (who is another employee) and this manager is given as an argument to the constructor.
class Worker(Employee):
    def __init__(self, name: str, salary: float, manager: Employee) -> None:
        """
        Initialise a new Worker instance.

        Parameters:
            name (str): The worker's name.
            salary (float): The worker's annual salary.
            manager (Employee): The worker's manager.
        """

        super().__init__(name, salary)
        self._manager = manager

    def get_manager(self) -> Employee:
        """
        (Employee) Return the manager.
        """

        return self._manager


# Define a subclass of Employee called Executive. An executive has a yearly bonus in addition to a wage and this bonus is given as an argument to the constructor.
class Executive(Employee):
    def __init__(self, name: str, salary: float, bonus: float) -> None:
        """
        Initialise a new Executive instance.

        Parameters:
            name (str): The executive's name.
            salary (float): The executive's annual salary.
            bonus (float): The executive's annual bonus.

        Example:
            >>> burns = Employee('Mr. Burns', 1000000)

            >>> smithers = Worker('Waylon Smithers', 25000, burns)
            >>> smithers.get_manager() is burns
            True

            >>> executive = Executive('Joseph Bloggs', 510000, 10000)
            >>> executive.wage() # Executive bonus is 10000.
            20000.0
        """

        super().__init__(name, salary)
        self._bonus = bonus

    def wage(self) -> float:
        """
        (float) Return the forgnightly wage.
        """
        # Call Employee.wage from Executive.wage (using super) to get the correct result.
        return super().wage() + self._bonus / 26
