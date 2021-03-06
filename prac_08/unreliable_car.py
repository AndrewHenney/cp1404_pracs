from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name='', fuel=0, reliability=0.0):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, reliability={}".format(super().__str__(),
                                                             self.reliability)

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        random_number = random.randint(0,101)
        if float(random_number)<self.reliability:
            distance_driven = super().drive(distance)

        else:
            distance_driven=0

        return distance_driven