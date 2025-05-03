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
    def calculate_rental_cost(self):
        pass

    @abstractmethod
    def get_vehicle_type(self):
        pass


class Car(Vehicle):
    def __init__(self, rate: int, hours: int):
        self.rate = rate
        self.hours = hours

    def calculate_rental_cost(self):
        return self.rate * self.hours

    def get_vehicle_type(self):
        print("\n\n\n\n\n-------------------------START------------------------\nChosen Vehicle Type: Car\n")


class Bike(Vehicle):
    def __init__(self, hours: int, rate : int):
        self.hours = hours
        self.rate = rate

    def calculate_rental_cost(self):
        return self.rate * self.hours

    def get_vehicle_type(self):
        print("\n\n\n\n\n-------------------------START------------------------\nChosen Vehicle Type: Bike\n")


class Truck(Vehicle):
    def __init__(self, hours : int, rate : int):
        self.hours = hours
        self.rate = rate

    def calculate_rental_cost(self):
        return self.rate * self.hours

    def get_vehicle_type(self):
        print("\n\n\n\n\n-------------------------START------------------------\nChosen Vehicle Type: Truck\n")


class RentalService(ABC):

    @abstractmethod
    def total_rental_cost():
        pass

    @abstractmethod
    def available_vehicles():
        pass

    @abstractmethod
    def discounts():
        pass

######################################################################


class TruckRent(Truck, RentalService):
    def __init__(self, hours:int, rate=1000):
        super().__init__(hours, rate)

    def total_rental_cost(self):
        base_price = self.rate * self.hours
        print(f"Rental cost: {base_price}")
        discount = self.discounts()
        print(f"Total: {base_price - discount}")

    def available_vehicles(self):
                print("\n==================AVAILABLE VEHICLES==================\n\nBike\t\t\tCar\t\t\tTruck\n\n======================================================\n\n--------------------------END-----------------------")


    def discounts(self):
         if self.hours < 2:
            discount = 0
            print(f"Discount: {discount}")
            return discount
         elif self.hours >= 2:
            discount = self.calculate_rental_cost() * 0.2
            print(f"Discount: {discount}")
            return discount

class CarRent(Car, RentalService):
    def __init__(self, hours: int, rate=500):
        super().__init__(hours, rate)

    def total_rental_cost(self):
        base_price = self.rate * self.hours
        print(f"Rental cost: {base_price}")
        discount = self.discounts()
        print(f"Total: {base_price - discount}")

    def available_vehicles(self):
        print("\n==================AVAILABLE VEHICLES==================\n\nBike\t\t\tCar\t\t\tTruck\n\n======================================================\n\n--------------------------END-----------------------")

    def discounts(self):
        if self.hours < 2:
            discount = 0
            print(f"Discount: {self.discount}")
            return discount
        elif self.hours >= 2:
            discount = self.calculate_rental_cost() * 0.3
            print(f"Discount: {discount}")
            return discount


class BikeRent(Bike, RentalService):
    def __init__(self, hours: int, rate=50):
        super().__init__(hours, rate)

    def total_rental_cost(self):
        base_price = self.rate * self.hours
        print(f"Rental cost: {base_price}")
        discount = self.discounts()
        print(f"Total: {base_price - discount}")

    def available_vehicles(self):
        print("\n==================AVAILABLE VEHICLES==================\n\nBike\t\t\tCar\t\t\tTruck\n\n======================================================\n\n--------------------------END-----------------------")
    def discounts(self):
        if self.hours < 2:
            discount = 0
            print(f"Discount: {self.discount}")
            return discount
        elif self.hours >= 2:
            discount = self.calculate_rental_cost() * 0.4
            print(f"Discount: {discount}")
            return discount



# EXAMPLE USAGES

# BIKE RENTAL
rent_bike = BikeRent(3)
rent_bike.get_vehicle_type()
rent_bike.discounts()
rent_bike.total_rental_cost()
rent_bike.available_vehicles()


# CAR RENTAL
rent_car = CarRent(3)
rent_car.get_vehicle_type()
rent_car.discounts()
rent_car.total_rental_cost()
rent_car.available_vehicles()


#TRUCK RENTAL
rent_truck = TruckRent(3)
rent_truck.get_vehicle_type()
rent_truck.discounts()
rent_truck.total_rental_cost()
rent_truck.available_vehicles()