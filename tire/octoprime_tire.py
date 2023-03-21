from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3
