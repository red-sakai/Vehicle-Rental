"""
LABORATORY EXERCISE #7
"""

"""
FEATURES LIST:
1. Each vehicle must have different rental cost rules, e.g. trucks are more expensive than bikes
2. RentalService class must:
   - List available vehicles.
   - Calculate the total rental cost for selected vehicles
   - Include discounts for rentals over a certain number of hours
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def calculate_rental_cost(hours):
        pass

    @abstractmethod
    def get_vehicle_type():
        pass


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


class Truck(Vechicle):
    pass


class RentalService(Vehicle):
    pass