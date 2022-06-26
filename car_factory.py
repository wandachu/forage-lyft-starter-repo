from component.engine.capulet_engine import CapuletEngine
from component.engine.sternman_engine import SternmanEngine
from component.engine.willoughby_engine import WilloughbyEngine

from component.battery.spindler_battery import SpindlerBattery
from component.battery.nubbin_battery import NubbinBattery

from component.tire.carrigan_tire import CarriganTire
from component.tire.octoprime_tire import OctoprimeTire


class CarFactory():

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(sensor_array)
        return Car(engine, battery, tire)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(sensor_array)
        return Car(engine, battery, tire)

    def create_palindrome(self, current_date, last_service_date, warning_light_on, sensor_array):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(sensor_array)
        return Car(engine, battery, tire)

    def  create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(sensor_array)
        return Car(engine, battery, tire)

    def  create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(sensor_array)
        return Car(engine, battery, tire)