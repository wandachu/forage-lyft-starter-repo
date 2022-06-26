from tire import Tire


class OctoprimeTire(Tire):

    SENSOR_THRESHOLD = 3

    def __init__(self, arr):
        self.sensor_array = arr
    

    def needs_service(self):
        return sum(self.sensor_array) >= self.SENSOR_THRESHOLD