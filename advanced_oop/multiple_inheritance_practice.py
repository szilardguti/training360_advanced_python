class Person:
    def __init__(self, name: str, email: str) -> None:
        self._name = name
        self._email: str = email

    def show(self) -> None:
        print(f"{self._name} ({self._email})")


class Address:
    def __init__(self, street: str, city: str) -> None:
        self.street = street
        self.city: str = city

    def show(self) -> None:
        print(f"{self.city} city; {self.street} street")


class Contact(Person, Address):
    def __init__(self, name: str, email: str, street: str, city: str) -> None:
        Person.__init__(self, name=name, email=email)
        Address.__init__(self, street=street, city=city)

    def show(self) -> None:
        Person.show(self)
        Address.show(self)


class Notebook:
    people: dict[str, Contact] = dict()

    def add(self, name: str, email: str, street: str, city: str) -> None:
        if name not in self.people.keys():
            contact = Contact(name, email, street, city)
            self.people[name] = contact

    def show(self, name: str) -> None:
        if name not in self.people.keys():
            print(f"Unknown {name}")
            return

        contact = self.people[name]
        contact.show()


notes = Notebook()

notes.add("Alice", "<al@kth.se>", "Lv 24", "Sthlm")
notes.add("Bob", "<bb@kth.se>", "Rtb 35", "Sthlm")

notes.show("Alice")
notes.show("Carol")


# Kimenet:

# Alice <al@kth.se>
# Lv 24
# Sthlm

# Unknown Carol
