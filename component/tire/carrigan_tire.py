from tire import Tire


class CarriganTire(Tire):

    SENSOR_THRESHOLD = 0.9

    def __init__(self, arr):
        self.sensor_array = arr
    

    def needs_service(self):
        for i in self.sensor_array:
            if (i >= self.SENSOR_THRESHOLD):
                return True
        return False