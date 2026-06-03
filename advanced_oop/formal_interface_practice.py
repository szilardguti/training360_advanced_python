import abc


class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self) -> None:
        raise NotImplementedError()


class Parrot(Bird):
    def fly(self) -> None:
        print("kakaw, parrot is flying!")


class Hero(abc.ABC):
    @abc.abstractmethod
    def fly(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def use_power(self) -> None:
        raise NotImplementedError()


class SuperMan(Hero):
    def fly(self) -> None:
        print("super fly!")

    def use_power(self) -> None:
        print("super power!")


# Ellenőrzés képpen futtasd le az alábbi kódot:
p = Parrot()
p.fly()  # slow flyer

super_man = SuperMan()
super_man.use_power()  # super

print(isinstance(p, Hero))  # False
print(isinstance(super_man, Bird))  # False
