from tires.tires import Tires

class CarriganTires(Tires):
	def __init__(self, tires):
		self.tires = tires

	def need_service(self):
		for t in tires:
			if t >= 0.9:
				return True
		return False