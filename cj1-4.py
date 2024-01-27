class Horse:
	def __init__(self, arms, legs, eyes, tail, furry):
		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.furry = furry

	def member(self):
		print(self.arms + " The length of the arms")
		print(self.legs + " The length of the legs")
		print(self.eyes + " The number of eyes")
		print(self.tail + " It has a tail")
		print(self.furry + " It is furry")
