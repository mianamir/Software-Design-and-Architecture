import string
import random

"""
This example code has strong Cohesion and less Coupling based on GRASP Princples 
of object-oriented design(OOD). 
"""

class VehicleInfo:

    def __init__(self, brand, electric, catalogue_price) -> None:
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def get_tax_clause_percentage(self) -> float:
        tax_percentage = 0.09
        if self.electric:
            tax_percentage = 0.04
        return tax_percentage

    def compute_tax(self) -> float:
        return self.get_tax_clause_percentage() * self.catalogue_price

    def get_vehicle_details(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:

    def __init__(self, id, license_plate, info) -> None:
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def get_vehicle_details(self) -> None:
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.get_vehicle_details()


class VehicleRegistry:

    def __init__(self) -> None:
        self.vehicle_info = {}
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)
        self.add_vehicle_info("Ford 2022", True, 95000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand) -> Vehicle:
        id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(id)
        return Vehicle(id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: string) -> None:
        # create a registry instance
        registry = VehicleRegistry()

        vehicle = registry.create_vehicle(brand)

        # get the vehicle information
        vehicle.get_vehicle_details()


if __name__ == '__main__':
    app = Application()
    app.register_vehicle("Ford 2022")
