# inheritance_demo.py
# A simple Python script demonstrating class inheritance.

# --- 1. Parent Class (Base Class) ---
class Animal:
    """
    The base class representing a generic animal.
    It has basic attributes and a common method.
    """
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def speak(self):
        """A generic method that all animals might override."""
        return f"The {self.species} named {self.name} makes a sound."

    def describe(self):
        """A common method inherited by all subclasses."""
        return f"This is an animal of species: {self.species}, named {self.name}."

# --- 2. Child Class (Derived Class) ---
class Dog(Animal):
    """
    The derived class representing a dog.
    It inherits attributes and methods from Animal and adds its own specific features.
    """
    def __init__(self, name, breed):
        # Call the parent class's constructor to initialize inherited attributes (species and name)
        # We explicitly set 'species' to 'Canis familiaris' for all Dog instances
        super().__init__(species="Canis familiaris", name=name)
        self.breed = breed
        self.can_fetch = True # A new attribute specific to Dog

    # Method Overriding: The Dog class provides its own implementation of the 'speak' method
    def speak(self):
        """Overrides the parent's speak method with a dog-specific sound."""
        return f"{self.name} the {self.breed} says: Woof! Woof!"

    # New Method: A method specific to the Dog class
    def fetch(self):
        if self.can_fetch:
            return f"{self.name} is happy and fetching the ball!"
        else:
            return f"{self.name} is not trained to fetch."

# --- 3. Demonstration ---
print("--- Inheritance Demonstration ---")

# Create an instance of the Parent Class
generic_animal = Animal(species="Feline", name="Mittens")
print("\n--- Parent Class Instance (Animal) ---")
print(generic_animal.describe())
print(generic_animal.speak())


# Create an instance of the Child Class
my_dog = Dog(name="Buddy", breed="Golden Retriever")
print("\n--- Child Class Instance (Dog) ---")
# 1. Accessing inherited methods (describe)
print(my_dog.describe())

# 2. Calling overridden method (speak)
print(my_dog.speak())

# 3. Calling a unique method (fetch)
print(my_dog.fetch())

# 4. Checking attributes
print(f"Species (Inherited): {my_dog.species}")
print(f"Breed (Unique to Dog): {my_dog.breed}")

print("\n--- End Demonstration ---")
