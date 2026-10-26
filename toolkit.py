import random


# Calculate two numbers using addition, subtraction, multiplication, or division.
def simple_calculator():
	try:
		first_number = float(input(f"Enter the first number: "))
		operator = input(f"Choose an operation (+, -, *, /): ").strip()
		second_number = float(input(f"Enter the second number: "))

		if operator == "+":
			result = first_number + second_number
		elif operator == "-":
			result = first_number - second_number
		elif operator == "*":
			result = first_number * second_number
		elif operator == "/":
			if second_number == 0:
				print(f"You can't divide by zero.")
				return
			result = first_number / second_number
		else:
			print(f"Sorry, that operation isn't supported.")
			return

		print(f"Result: {result}")
	except ValueError:
		print(f"Please enter valid numbers.")


# Add, view, and remove tasks from a list that lasts while this tool is open.
def todo_list():
	tasks = []
	while True:
		print(f"\nTo-do list")
		print(f"1. Add a task")
		print(f"2. View tasks")
		print(f"3. Remove a task")
		print(f"4. Return to the main menu")
		choice = input(f"Choose an action (1-4): ").strip()

		if choice == "1":
			task = input(f"What task would you like to add? ").strip()
			if task:
				tasks.append(task)
				print(f"Added '{task}' to your list.")
			else:
				print(f"Please enter a task to add.")
		elif choice == "2":
			if tasks:
				for index, task in enumerate(tasks, start=1):
					print(f"{index}. {task}")
			else:
				print(f"Your list is empty for now.")
		elif choice == "3":
			if tasks:
				for index, task in enumerate(tasks, start=1):
					print(f"{index}. {task}")
				try:
					task_number = int(input(f"Enter the task number to remove: "))
					if 1 <= task_number <= len(tasks):
						removed_task = tasks.pop(task_number - 1)
						print(f"Removed '{removed_task}' from your list.")
					else:
						print(f"Please choose a number shown in your list.")
				except ValueError:
					print(f"Please enter a whole-number task number.")
			elif not tasks:
				print(f"Your list is empty, so there is nothing to remove.")
		elif choice == "4":
			print(f"Returning to the main menu.")
			return
		else:
			print(f"Sorry, that's not a to-do menu option. Please choose 1, 2, 3, or 4.")


# Guess a randomly chosen number and get higher-or-lower hints.
def number_guessing_game():
	secret_number = random.randint(1, 100)
	print(f"I'm thinking of a number from 1 to 100.")

	while True:
		try:
			guess = int(input(f"Enter your guess: "))
		except ValueError:
			print(f"Please enter a whole number.")
			continue

		if guess < secret_number:
			print(f"Too low. Try again!")
		elif guess > secret_number:
			print(f"Too high. Try again!")
		else:
			print(f"Correct! The number was {secret_number}.")
			return


def main():
	print(f"Welcome to the Toolkit! Choose a tool to get started.")
	while True:
		print(f"\nToolkit")
		print(f"1. Simple calculator")
		print(f"2. To-do list")
		print(f"3. Number-guessing game")
		print(f"4. Quit")
		choice = input(f"Choose a tool (1-4): ").strip()

		if choice == "1":
			simple_calculator()
		elif choice == "2":
			todo_list()
		elif choice == "3":
			number_guessing_game()
		elif choice == "4":
			print(f"Goodbye!")
			break
		else:
			print(f"Sorry, that's not a menu option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
	main()



