"""
This class contains methods to create different types of cars
"""
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        car_engine = CapuletEngine(current_mileage, last_service_mileage)
        car_battery = SpindlerBattery(last_service_date, current_date)
        car_tires = CarriganTire(tire_wear)
        return Car(car_engine, car_battery, car_tires)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        car_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car_battery = SpindlerBattery(last_service_date, current_date)
        car_tires = OctoprimeTire(tire_wear)
        return Car(car_engine, car_battery, car_tires)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        car_engine = SternmanEngine(warning_light_on)
        car_battery = SpindlerBattery(last_service_date, current_date)
        car_tires = CarriganTire(tire_wear)
        return Car(car_engine, car_battery, car_tires)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        car_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car_battery = NubbinBattery(last_service_date, current_date)
        car_tires = OctoprimeTire(tire_wear)
        return Car(car_engine, car_battery, car_tires)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        car_engine = CapuletEngine(current_mileage, last_service_mileage)
        car_battery = NubbinBattery(last_service_date, current_date)
        car_tires = CarriganTire(tire_wear)
        return Car(car_engine, car_battery, car_tires)
