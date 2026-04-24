import random
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node2D import Node2D

@gdclass
class NumberGuessingGame(Node2D):

	def _ready(self) -> None:
		self.num_input = self.get_node("../CanvasLayer/Input")
		self.guesses_remaining_label = self.get_node("../CanvasLayer/GuessesRemaining")
		self.hint_label = self.get_node("../CanvasLayer/HintLabel")
		
		self.target = random.randint(0,100)
		self.guesses_remaining = 5
		self.hint_label.text = str(self.target)\
		
		self.guesses_remaining_label.text = str(self.guesses_remaining)
		
		self.num_input.grab_focus()
		self.num_input.value_changed.connect(self._on_input_changed)
		
		
	def _process(self, delta:float) -> None:
		pass
	
	@property
	def get_target(self):
		return self.target

	def _on_input_changed(self, new_value: float):
		if not isinstance(new_value,float):
			print("Invalid Input")
		if new_value == self.target:
			self.hint_label.text = "You Win"
		elif new_value < self.target:
			self.hint_label.text = "Higher"
		elif new_value > self.target:
			self.hint_label.text = "Lower"
		self.guesses_remaining -= 1
		self.guesses_remaining_label.text = str(self.guesses_remaining)
