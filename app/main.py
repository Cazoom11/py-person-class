class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    Person.people = {}
    for item in people:
        person = Person(item["name"], item["age"])
        Person.people[item["name"]] = person

    for item in people:
        person = Person.people[item["name"]]

        wife = item.get("wife")
        if wife:
            person.wife = Person.people[wife]

        husband = item.get("husband")
        if husband:
            person.husband = Person.people[husband]
    return list(Person.people.values())
