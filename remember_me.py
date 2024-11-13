import json

# Программа загружаеть имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает его и сохраняет.

def greet_user():
	"""Приветствует пользователя по имени"""
	filename = 'username.json'
	try:
		with open(filename) as f:
			user_info = json.load(f)
	except FileNotFoundError:
		username = input("Как твое имя сынок ?")
		with open(filename, f) as f:
			json.dump(username, f)
			print(f"We'll remember you when come back, {username}!")
	else:
		print(f"Welcome back, {username}!")

greet_user()