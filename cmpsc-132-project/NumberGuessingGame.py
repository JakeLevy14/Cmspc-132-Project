import random
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node2D import Node2D

@gdclass
class NumberGuessingGame(Node2D):

	def _ready(self) -> None:
		self.label = self.get_node("../Label")
		self.target = random.randint(0,100)
		self.label.text = str(self.get_target)


	def _process(self, delta:float) -> None:
		pass
	
	@property
	def get_target(self):
		return self.target
		
