import random
import time

time.sleep(0.5)
print("Every typo while playing this game will be set as 'DRAW'")

def ask_ques1():
	ask1 = input("What do you want to choose? (rock, paper, scissors, lizard, spock) \n")
	return ask1

again = 'YES'
while again == 'YES' or again == 'Y':
	option = ['rock', 'paper', 'scissors', 'lizard', 'spock']

	def randomchoice(option):
		choice = random.choice(option)
		return choice
		
	choice = randomchoice(option)
	def ans():
		answer = print("The computer has: " + str(choice))
		return answer
	R = " rock "
	P = " paper "
	Sc = " scissors "
	Sp = " spock "
	L = " lizard "
	
	user = ask_ques1()
	if user == choice:
		ans()
		print("DRAW!")
	
	
	elif choice == 'rock':
		if user == 'lizard' or user == 'scissors':
			if user == 'lizard':
				ans()
				print("The " + R + " crushes " + L + " ===> You lost!!!")
			else:
				ans()
				print("The " + R + " crushes " + Sc + " ===> You lost!!!")
		elif user == 'spock' or user == 'paper':
			if user == 'spock':
				ans()
				print("The " + Sp + " vaporizes " + R + " ===> You won!!!")
			else:
				ans()
				print("The " + P + " covers " + R + " ===> You won!!!")
		else:
			ans()
			print("DRAW")
	
	
	
	elif choice == 'paper':
		if user == 'rock' or user == 'spock':
			if user == 'rock':
				ans()
				print("The " + P + " covers " + R + " ===> You lost!!!")
			else:
				ans()
				print("The " + P + " disproves " + Sp + " ===> You lost!!!")
		elif user == 'scissors' or user == 'lizard':
			if user == 'scissors':
				ans()
				print("The " + Sc + " cuts " + P + " ===> You won!!!")
			else:
				ans()
				print("The " + L + " eats " + P + " ===> You won!!!")
		else:
			ans()
			print("DRAW")
	
	
	
	elif choice == 'scissors':
		if user == 'lizard' or user == 'paper':
			if user == 'lizard':
				ans()
				print("The " + Sc + " decapitates " + L + " ===> You lost!!!")
			else:
				ans()
				print("The " + Sc + " cuts " + P + " ===> You lost!!!")
		elif user == 'spock' or user == 'rock':
			if user == "spock":
				ans()
				print("The " + Sp + " smashes " + Sc + " ===> You won!!!")
			else:
				ans()
				print("The " + R + " crushes " + Sc + " ===> You won!!!")
		else:
			ans()
			print("DRAW")
	
	
	
	elif choice == 'spock':
		if user == 'scissors' or user == 'rock':
			if user == 'scissors':
				ans()
				print("The " + Sp + " smashes " + Sc + " ===> You lost!!!")
			else:
				ans()
				print("The " + R + " crushes " + Sc + " ===> You lost!!!")
		elif user == 'lizard' or user == 'paper':
			if user == 'lizard':
				ans()
				print("The " + L + " poisons " + Sp + " ===> You won!!!")
			else:
				ans()
				print("The " + P + " disproves " + Sp + " ===> You won!!!")
		else:
			ans()
			print("DRAW")
	
	
	
	else:
		if user == 'paper' or user == 'spock':
			if user == 'paper':
				ans()
				print("The " + L + " eats " + P + " ===> You lost!!!")
			else:
				ans()
				print("The " + L + " poisons " + Sp + " ===> You lost!!!")
		elif user == 'scissors' or user == 'rock':
			if user == 'scissors':
				ans()
				print("The " + Sc + " decapitates " + L + " ===> You won!!!")
			else:
				ans()
				print("The " + R + " crushes " + L + " ===> You won!!!")
		else:
			ans()
			print("DRAW")

	again = input("Do you want to play again? (Y/N) \n").upper()
print("Thanks for playing")

