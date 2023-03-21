"""
This class contains methods to create different types of cars
"""
from car import Car
from engine import *
from battery import *

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = capulet_engine(current_mileage, last_service_mileage)
        car_battery = spindler_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = willoughby_engine(current_mileage, last_service_mileage)
        car_battery = spindler_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)

    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = sternman_engine(current_mileage, last_service_mileage)
        car_battery = spindler_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = willoughby_engine(current_mileage, last_service_mileage)
        car_battery = nubbin_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = capulet_engine(current_mileage, last_service_mileage)
        car_battery = nubbin_battery(last_service_date, current_date)
        return Car(car_engine, car_battery)
