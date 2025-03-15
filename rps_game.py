import random

print("Welcome to rock paper scissors game.")
user=0
x=0
computer=0
options=["Rock","Paper","Scissors"]

while x<3:
	print("------------------------------------------")
	user_choice = int(input("0: Rock | 1: Paper | 2: Scissors -> "))
	print("------------------------------------------")
	computer_choice = random.randint(0,2)
	if user_choice not in [0,1,2]:
		print("Invalid value try again...")
		continue
	if(user_choice==computer_choice):
		user=user+1
		computer=computer+1
		print(f"You choose: {options[user_choice]}, Computer choose: {options[computer_choice]}")
		print(f"You: {user} | Computer: {computer}")
	elif(user_choice==0 and computer_choice==1):
		computer=computer+1
		print(f"You choose: {options[user_choice]}, Computer choose: {options[computer_choice]}")
		print(f"You: {user} | Computer: {computer}")
	elif(user_choice==0 and computer_choice==2):
		user=user+1
		print(f"You choose: {options[user_choice]}, Computer choose: {options[computer_choice]}")
		print(f"You: {user} | Computer: {computer}")
	elif(user_choice==1 and computer_choice==0):
		user=user+1
		print(f"You choose: {options[user_choice]}, Computer choose: {options[computer_choice]}")
		print(f"You: {user} | Computer: {computer}")
	elif(user_choice==1 and computer_choice==2):
		computer= computer+1
		print(f"You choose: {options[user_choice]}, Computer choose: {options[computer_choice]}")
		print(f"You: {user} | Computer: {computer}")
	elif(user_choice==2 and computer_choice==0):
		computer=computer+1
		print(f"You choose: {options[user_choice]}, Computer choose: {options[computer_choice]}")
		print(f"You: {user} | Computer: {computer}")
	elif(user_choice==2 and computer_choice==1):
		user=user+1
		print(f"You choose: {options[user_choice]}, Computer choose: {options[computer_choice]}")
		print(f"You: {user} | Computer: {computer}")
	x=x+1;


if(user>computer):
	print("You win")
elif(computer>user):
	print("You lost")
else:
	print("It is a draw")