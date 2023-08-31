from __future__ import annotations


class Person(object):
    def __init__(self, name: str, age: int, gender: str):
        """Construct a person object given their name, age and gender"""

        self._name = name
        self._age = age
        self._gender = gender
        self._friend = None

    def __eq__(self, person: Person) -> bool:
        return str(self) == str(person)

    def __str__(self) -> str:
        if self._gender == "M":
            title = "Mr"
        elif self._gender == "F":
            title = "Miss"
        else:
            title = "M"

        return title + " " + self._name + " " + str(self._age)

    def __repr__(self) -> str:
        return "Person: " + str(self)

    def get_name(self) -> str:
        """
        (str) Return the name

        """
        return self._name

    def get_age(self) -> str:
        """
        (int) Return the age

        """
        return self._age

    def get_gender(self) -> str:
        """
        (str) Return the gender

        """
        return self._gender

    def set_friend(self, friend: Person) -> str:
        self._friend = friend

    def get_friend(self):
        """
        (Person) Return the friend

        """
        return self._friend


def print_friend_info(person: Person) -> None:
    """print_friend_info Prints the info list of a person.

    Example:
    >>> fry = create_fry()
    >>> print_friend_info(fry)
    Philip J. Fry
    25

    >>> alice = Person('Alice Liddell', 8, 'F')
    >>> make_friends(alice, fry)
    >>> print_friend_info(alice)
    Alice Liddell
    8
    Friends with Philip J. Fry
    """
    name = person.get_name()
    age = person.get_age()
    print(name)
    print(age)
    friend = person.get_friend()
    if friend is not None:
        print(f"Friends with {friend.get_name()}")


def create_fry() -> Person:
    """create_fry Creates a person (for example, Fry)
    >>> fry = create_fry()
    >>> print_friend_info(fry)
    Philip J. Fry
    25
    """
    fry = Person("Philip J. Fry", 25, "M")
    return fry


def make_friends(person1: Person, person2: Person) -> None:
    """make_friends Makes person1 and person2 friends with Fry.



    Args:
        person1 (Person): Person 1
        person2 (Person): Person 2

    >>> alice = Person('Alice Liddell', 8, 'F')
    >>> make_friends(alice, fry)
    >>> print_friend_info(alice)
    Alice Liddell
    8
    Friends with Philip J. Fry
    """
    person1.set_friend(person2)
    person2.set_friend(person1)
