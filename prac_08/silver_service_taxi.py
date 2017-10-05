from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    price_per_km = 1.23
    flagfall=4.50
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, fanciness = 1):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km *fanciness
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km, self.flagfall)
    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall