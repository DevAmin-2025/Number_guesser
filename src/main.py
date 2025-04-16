import random

from src.utils import (print_excellent, print_information, print_medium,
                       print_week)

random.seed(10)

class NumberGuesser:
	def __init__(self):
		self.score = 100
		self.selected_number = self.generate_random_number(1, 100)

	def validate_input(self, user_guess: str) -> bool:
		"""
		Check if the input from user is valid
		And print messages accordingly.

		:param user_guess: Input user guess.
		:return: True if input is valid, False if is not.
		"""
		try:
			user_guess = int(user_guess)
			if not 1 <= user_guess <= 100:
				print_information(f'The number must be between 1 to 100. Yours is {user_guess}')
				return False
			return True
		except ValueError:
			print_information('Invalid input')
			return False

	def generate_random_number(self, start: int, end: int) -> int:
		"""
		Generate a random number.

		:param start: Input start point for generating random number.
		:param end: Input end point for generating random number.
		:return: Return a random number within the range of start and end numbers.
		"""
		selected_number = random.randint(start, end)
		return selected_number

	def play_again(self) -> bool:
		"""
		Determine whether user wants to play again or not.

		:param user_choice: Input user choice
		:return: Return True if the user wants to play again and False if he/she does not.
		"""
		user_choice = input('Do you want to play again? (y/n): ').lower()
		if user_choice == 'n':
			print_information('Goodbye!')
			return False
		elif user_choice == 'y':
			self.score = 100
			self.selected_number = self.generate_random_number(1, 100)
			return True
		else:
			print_information('Invalid input')
			print_information('Goodbye!')
			return False

	def start_game(self):
		"""
		Run the main flow of the game and handle prompting the user for a number,
		Check if the number meets the predefined criteria and keep prompting the user
		For numbers until the game ends.
		"""
		while True:
			user_guess = input('Please guess a number between 1 to 100 (or q to exit): ')
			if user_guess.lower() == 'q':
				print_information('Goodbye!')
				break
			elif not self.validate_input(user_guess):
				continue

			user_guess = int(user_guess)
			if user_guess > self.selected_number:
				print_information('Your guess is too high. Please try again.')
			elif user_guess < self.selected_number:
				print_information('Your guess is too low. Please try again.')
			else:
				print_excellent('Congratulations! Your guess was correct.')
				if self.score >= 70:
					print_excellent(f'Your score: {self.score}')
				elif self.score >= 40:
					print_medium(f'Your score: {self.score}')
				else:
					print_week(f'Your score: {self.score}')

				if not self.play_again():
					break
				else:
					continue

			self.score -= 10
			if self.score == 0:
				print_week(f'Game over! The number was: {self.selected_number}')
				if not self.play_again():
					break
				else:
					continue


if __name__ == '__main__':
	game = NumberGuesser()
	game.start_game()
