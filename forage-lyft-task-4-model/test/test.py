import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestCapuletEngine(unittest.TestCase):
	def test_engine_should_be_serviced(self):
		current_mileage = 30001
		last_service_mileage = 0

		engine = CapuletEngine(current_mileage, last_service_mileage)
		self.assertTrue(engine.need_service())

	def test_engine_should_not_be_serviced(self):
		current_mileage = 30000
		last_service_mileage = 0

		engine = CapuletEngine(current_mileage, last_service_mileage)
		self.assertFalse(engine.need_service())

class TestSternmanEngine(unittest.TestCase):
	def test_engine_should_be_serviced(self):
		warning_light_is_on = True

		engine = SternmanEngine(warning_light_is_on)
		self.assertTrue(engine.need_service())

	def test_engine_should_not_be_serviced(self):
		current_mileage = False

		engine = SternmanEngine(current_mileage)
		self.assertFalse(engine.need_service())


class TestWilloughbyEngine(unittest.TestCase):
	def test_engine_should_be_serviced(self):
		current_mileage = 60001
		last_service_mileage = 0

		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		self.assertTrue(engine.need_service())

	def test_engine_should_not_be_serviced(self):
		current_mileage = 60000
		last_service_mileage = 0

		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		self.assertFalse(engine.need_service())


class TestNubbinBattery(unittest.TestCase):
	def test_battery_should_be_serviced(self):
		today = datetime.today().date()
		last_service_date = today.replace(year=today.year - 5)

		battery = NubbinBattery(today, last_service_date)
		self.assertTrue(battery.need_service())

	def test_battery_should_not_be_serviced(self):
		today = datetime.today().date()
		last_service_date = today.replace(year=today.year - 3)

		battery = NubbinBattery(today, last_service_date)
		self.assertFalse(battery.need_service())


class TestSpindlerBattery(unittest.TestCase):
	def test_battery_should_be_serviced(self):
		today = datetime.today().date()
		last_service_date = today.replace(year=today.year - 4)

		battery = SpindlerBattery(today, last_service_date)
		self.assertTrue(battery.need_service())

	def test_battery_should_not_be_serviced(self):
		today = datetime.today().date()
		last_service_date = today.replace(year=today.year - 2)

		battery = SpindlerBattery(today, last_service_date)
		self.assertFalse(battery.need_service())
