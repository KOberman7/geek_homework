class Road:

	layer = 5
	kl_g = 25
	
	def __init__(self):
		self._length = 20
		self._width = 5000
		self.result = self._width * self._length * self.kl_g * self.layer

R = Road()
print(R.result)