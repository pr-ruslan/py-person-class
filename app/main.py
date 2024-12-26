class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = Person(
            name=self.name,
            age=self.age
        )


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(
            name=person["name"],
            age=person["age"]
        ))

    def add_partner() -> None:
        nonlocal person
        for person in people:
            if person[wife]
            for listed_person in person_list:


    return person_list
