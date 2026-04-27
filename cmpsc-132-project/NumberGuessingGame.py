import random
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node2D import Node2D

@gdclass
class NumberGuessingGame(Node2D):

	def _ready(self) -> None:
		self.guessing_layer = self.get_node("../GuessingLayer")
		self.num_input = self.get_node("../GuessingLayer/Input")
		self.guesses_remaining_label = self.get_node("../GuessingLayer/GuessesRemaining")
		self.hint_label = self.get_node("../GuessingLayer/HintLabel")
		self.up_arrow = self.get_node("../GuessingLayer/Uparrow")
		self.down_arrow = self.get_node("../GuessingLayer/DownArrow")
		self.win_layer = self.get_node("../WinLayer")
		self.lose_layer = self.get_node("../LoseLayer")
		self.try_again_button = self.get_node("../TryAgainButton")
		self.menu_layer = self.get_node("../MenuLayer")
		self.difficulty_layer = self.get_node("../DifficultyLayer")
		self.target_label = self.get_node("../Target")
		
		

	def _on_input_changed(self, new_value: float):
		if not isinstance(new_value,float):
			print("Invalid Input")
		if new_value == self.target:
			self.target_label.visible = True
			self.try_again_button.visible = True
			self.guessing_layer.visible = False
			self.win_layer.visible = True
			self.try_again_button.visible = True
			self.target_label.text += "\n" + str(self.target)
		elif new_value < self.target:
			self.hint_label.text = "Higher"
			self.up_arrow.visible = True
			self.down_arrow.visible = False
		elif new_value > self.target:
			self.hint_label.text = "Lower"
			self.up_arrow.visible = False
			self.down_arrow.visible = True
		self.guesses_remaining -= 1
		self.guesses_remaining_label.text = str(self.guesses_remaining)
		if self.guesses_remaining == 0:
			self.target_label.visible = True
			self.try_again_button.visible = True
			self.lose_layer.visible = True
			self.guessing_layer.visible = False
			self.target_label.text += "\n" + str(self.target)

	def _on_easy_button_pressed(self):
		self.difficulty = "Easy"
		self.num_input.max_value = 50
		self.guesses_remaining = 7
		self.target = random.randint(0,51)
		self.gameSetup(self.difficulty,self.guesses_remaining,self.target)
	
	def _on_normal_button_pressed(self):
		self.difficulty = "Normal"
		self.num_input.max_value = 100
		self.guesses_remaining = 8
		self.target = random.randint(0,101)
		self.gameSetup(self.difficulty,self.guesses_remaining,self.target)

	def _on_hard_button_pressed(self):
		self.difficulty = "Hard"
		self.num_input.max_value = 999
		self.guesses_remaining = 10
		self.target = random.randint(0,1000)
		self.gameSetup(self.difficulty,self.guesses_remaining,self.target)
		
	def gameSetup(self,difficulty,guesses,target):
		self.guessing_layer.visible = True
		self.difficulty_layer.visible = False
		self.hint_label.text = difficulty
		self.guesses_remaining_label.text = str(self.guesses_remaining)
		
		self.num_input.grab_focus()
		self.num_input.value_changed.connect(self._on_input_changed)


	def _on_start_button_pressed(self):
		self.menu_layer.visible = False
		self.difficulty_layer.visible = True


	def _on_try_again_button_pressed(self):
		self.get_tree().reload_current_scene()
