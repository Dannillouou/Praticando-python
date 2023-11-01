class Animal:
    """
    This is the base class for all animals.
    """

    def __init__(self, name, species) -> None:
        """
        Constructor to initialize an animal object.

        Args:
            name (str): The name of the animal
            species (str): The species of the animal
        """
        self.name = name
        self.species = species

    def speak(self):
        """
        Make the animal speak.

        Returns:
            str: A message representing the animal's speech.
        """      
        return f"{self.name} says Hi!"
    
    # sobrescreve a representação em forma de string que todo objeto em python tem
    def __str__(self) -> str:
        """
        String representation of the animal.

        Returns:
            str: A string with the animal's
        """

    # também funciona como uma representação em forma de texto do objeto
    # a diferença entre str e repr está no fato de que str printa o obje
    # to de uma maneira mais legível, enquanto repr procura representar
    # o objeto de forma que seja fácil entender do que ele se trata
    def __repr__(self) -> str:
        pass

class Dog(Animal):
    """
    A class representing a Dog, inheriting from the Animal class.
    """

    def __init__(self, name, breed) -> None:
        """
        Constructor to initialize a dog object.

        Args:
            name (str): The name of the animal.
            breed (str): The breed of the Dog.
        """
        # usando construtor da classe pai de chachorro (animal)
        super().__init__(name, species="Dog")

        self.breed = breed

    def Speak(self):
        """
        Make the dog bark.

        Returns:
            str: A message representing the dog's bark
        """
        return f"{self.name} barks, Woof!"
    
    def wag_tail(self):
        """
        Make the dog wag it's tail.

        Returns:
            str: A message representing the dog wagging it's tail
        """

class Cat(Animal):
    """
    A class representing a Cat, inheriting from the Animal class
    """

    def __init__(self, name, color) -> None:
        """
        Constructor to initialize a dog object.

        Args:
            name (str): The name of the animal.
            breed (str): The breed of the Dog.
        """
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        """
        Make the cat meow

        Returns:
            str: A message representing the cat's meow
        """

        return f"{self.name} meows, Miim!"
    
    def purr(self):
        """
        Make the cat purr.

        Returns:
            str: A message representing the cat purring
        """

# Creating instance of dog and Cat classes
my_dog = Dog("Chun li", "French bulldog")
my_cat = Cat("José", "Black")

# Call methods to demonstrate functionality
print(my_dog.speak())
print(my_dog.wag_tail())
print(my_cat.speak())
print(my_cat.purr())

# display information about the animal
print(my_dog)
print(my_cat)