import unittest
import vehicle


class VehicleTests(unittest.TestCase):
   def test_vehicle(self):
       car = vehicle.vehicle(4, 100, 2, False)
       self.assertEqual(car.wheels, 4)
       self.assertEqual(car.fuel, 100)
       self.assertEqual(car.doors, 2)
       self.assertEqual(car.roof, False)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

