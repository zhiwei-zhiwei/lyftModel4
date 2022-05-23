from tires.tires import Tires

class OctoprimeTires(Tires):
	def __init__(self, tires):
		self.tires = tires

	def need_service(self):
		count = 0
		for t in tires:
			count += t
		if count >= 3:
			return True
		else:
			return False