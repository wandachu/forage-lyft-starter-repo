from battery import Battery


class NubbinBattery(Battery):
    SERVICE_YEARS = 4

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.SERVICE_YEARS)
        return service_threshold_date < self.current_date