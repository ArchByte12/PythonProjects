# abstraction_demo.py
# A Python script demonstrating Abstraction using Abstract Base Classes (ABCs).

from abc import ABC, abstractmethod

# --- 1. Abstract Base Class (Blueprint) ---
# The ABC class provides the mechanism for abstract base classes.
class Vehicle(ABC):
    """
    An Abstract Base Class (ABC) for all vehicles.
    It defines a common interface (the abstract methods) that all derived classes MUST implement.
    """

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False

    # Abstract Method 1: All subclasses must define how to start the engine.
    @abstractmethod
    def start_engine(self):
        """Forces subclasses to implement engine starting logic."""
        pass

    # Abstract Method 2: All subclasses must define how they drive.
    @abstractmethod
    def drive(self):
        """Forces subclasses to implement driving/movement logic."""
        pass

    # Concrete Method: This method is inherited and can be used directly.
    def show_info(self):
        """A concrete method providing common information."""
        print(f"Vehicle: {self.make} {self.model}")
        print(f"Engine Status: {'Running' if self.is_running else 'Off'}")


# --- 2. Concrete Class 1 (Must implement all abstract methods) ---
class Car(Vehicle):
    """
    Concrete class for a Car. It provides the specific implementation details
    for the abstract methods defined in Vehicle.
    """
    def start_engine(self):
        print(f"{self.make} {self.model}: Starting the ignition and fuel pump sequence...")
        self.is_running = True
        print("Engine started with a gentle purr.")

    def drive(self):
        if self.is_running:
            print(f"{self.make} {self.model}: Shifting into drive and cruising on four wheels.")
        else:
            print("Cannot drive. Please start the engine first.")

# --- 3. Concrete Class 2 (Must implement all abstract methods) ---
class Motorcycle(Vehicle):
    """
    Concrete class for a Motorcycle. Its implementation of abstract methods
    is different from the Car.
    """
    def start_engine(self):
        print(f"{self.make} {self.model}: Pulling the choke and kicking the starter pedal...")
        self.is_running = True
        print("Engine roared to life!")

    def drive(self):
        if self.is_running:
            print(f"{self.make} {self.model}: Leaning into the curve on two wheels.")
        else:
            print("Cannot drive. Please start the engine first.")


# --- 4. Demonstration ---
print("--- Abstraction Demonstration ---")

# We cannot instantiate the abstract class directly! Uncomment the line below to see the error:
# try:
#     abstract_vehicle = Vehicle("Generic", "Model")
# except TypeError as e:
#     print(f"Error when trying to instantiate Abstract Class: {e}")


print("\n--- Car Implementation ---")
my_car = Car("Toyota", "Camry")
my_car.show_info() # Inherited concrete method
my_car.start_engine() # Implementation specific to Car
my_car.drive() # Implementation specific to Car

print("\n--- Motorcycle Implementation ---")
my_bike = Motorcycle("Harley-Davidson", "Iron 883")
my_bike.show_info() # Inherited concrete method
my_bike.start_engine() # Implementation specific to Motorcycle
my_bike.drive() # Implementation specific to Motorcycle

print("\n--- The Abstraction ---")
print("Both Car and Motorcycle use the same interface (start_engine, drive, show_info),")
print("but the internal 'how' (the implementation details) is completely different and hidden.")
