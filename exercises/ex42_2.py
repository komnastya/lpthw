# !!! поля конструктора могут быть по умолчанию
# def __init__ (self) - это конструктор, который определяет структуру класса ("обозначает", каким изначально будет класс)
# это значит что все объекты созданные таким конструктором имеют одинаковую структуру и данные


class Mammal:
    def __init__(self, mammalName):  # вызывается неявно когда мы пишем Mammal ("Pig")
        self.name = mammalName
        print(mammalName, "is a mammal")
        self.isAnimal = "Mammal"
        print(self.isAnimal, "is a warm-blooded animal.")


class Cat(Mammal):
    def __init__(
        self, catName
    ):  # конструктор вызывается неявно когда мы пишем Cat("Tom")
        self.cat_name = catName
        super().__init__("Cat")  # здесь явно вызываем конструктор класса Mammal
        # чтобы создать структуру животного (класса Cat)
        self.eatsMice = True  # а теперь к животному добавить структуру
        # специфичную для кота
        print(self.name, self.cat_name, "eats mice!")


class BlackCat(Cat):
    def __init__(self, BlackCatName):
        super().__init__("Black")
        self.name = BlackCatName
        print("Cat ", self.name, " has a black skin")


pig = Mammal("Peppa")
elephant = Mammal("Elephant")
cat = Cat("Tom")
b_cat = BlackCat("Jack")
print("Pig name is", pig.name)
print("Cat name is", cat.cat_name)
print("Black cat name is", b_cat.name)
