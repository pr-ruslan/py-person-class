class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(
            name=person["name"],
            age=person["age"]
        ))

    def get_partner_pointer(partner_name: str) -> Person:
        nonlocal person_list
        for person in person_list:
            if person.name == partner_name:
                return person

    for i in range(len(person_list)):
        if "wife" in people[i]:
            if not people[i]["wife"]:
                continue
            else:
                person = person_list[i]
                person.wife = get_partner_pointer(people[i]["wife"])
        elif not people[i]["husband"]:
            continue
        else:
            person = person_list[i]
            person.husband = get_partner_pointer(people[i]["husband"])

    return person_list
