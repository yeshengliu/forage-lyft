"""
This class contains methods to create different types of cars
"""
from car import Car
from engine import *
from battery import *

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = capulet_engine(current_mileage, last_service_mileage)
        car_battery = spindler_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = willoughby_engine(current_mileage, last_service_mileage)
        car_battery = spindler_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = sternman_engine(current_mileage, last_service_mileage)
        car_battery = spindler_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = willoughby_engine(current_mileage, last_service_mileage)
        car_battery = nubbin_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = capulet_engine(current_mileage, last_service_mileage)
        car_battery = nubbin_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)
