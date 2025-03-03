class Animal:
    """ Создаю базовый класс для животных """

    def __init__(self, name: str, age: int):
        """

        Инициализирую животное

        :param name: Имя животного
        :param age: Возраст животного
        """
        self._name = name  # Имя животного (непубличный атрибут)
        self._age = age    # Возраст животного (непубличный атрибут)

    @property
    def name(self) -> str:
        """ Возвращает имя животного """

        return self._name

    @property
    def age(self) -> int:
        """ Возвращает возраст животного """

        return self._age

    def make_sound(self) -> str:
        """ Возвращает звук, который издаеет животное """

        return "Звук животного"

    def __str__(self) -> str:
        """ Возвращает представление животного """

        return f"{self.name}, возраст {self.age} лет"

    def __repr__(self) -> str:
        """ Возвращает представление животного """

        return f"Animal(name={self.name!r}, age={self.age!r})"


class Dog(Animal):
    """ Создаю класс для собак """

    def __init__(self, name: str, age: int, breed: str):
        """

        Инициализирую собаку

        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age)  # Вызываем конструктор базового класса
        self.breed = breed  # Порода собаки

    def make_sound(self) -> str:
        """ Возвращает звук, который издает собака
            Переопределение метода, чтобы указать специфичный звук для собаки
        """
        return "Гав!"

    def __str__(self) -> str:
        """ Возвращает представление собаки """
        return f"{super().__str__()}, порода {self.breed}"

    def __repr__(self) -> str:
        """ Возвращает представление собаки """
        return f"Dog(name={self.name!r}, age={self.age!r}, breed={self.breed!r})"


class Cat(Animal):
    """ Класс для кошек """

    def __init__(self, name: str, age: int, color: str):
        """
        Инициализирую кошку

        :param name: Имя кошки
        :param age: Возраст кошки
        :param color: Цвет кошки
        """
        super().__init__(name, age)  # Вызываем конструктор базового класса
        self.color = color  # Цвет кошки

    def make_sound(self) -> str:
        """ Возвращает звук, который издает кошка
            Переопределение метода, чтобы указать специфичный звук для кошки
        """

        return "Мяу!"

    def __str__(self) -> str:
        """ Возвращает представление о кощке """

        return f"{super().__str__()}, цвет {self.color}"

    def __repr__(self) -> str:
        """ Возвращает представление о кощке """

        return f"Cat(name={self.name!r}, age={self.age!r}, color={self.color!r})"


if __name__ == "__main__":
    dog = Dog("Шарик", 3, "Бульдог")
    cat = Cat("Мурка", 2, "Черный")
    print(dog)          # Выводит информацию о собаке
    print(cat)          # Выводит информацию о кошке
    print(dog.make_sound())  # Выводит звук собаки
    print(cat.make_sound())  # Выводит звук кошки
