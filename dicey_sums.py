#Importing turtle and random module from python
import turtle
import random
from time import *
import os
#Creating screen object from turtle
sc = turtle.Screen()
#wow
#Creating six turtles to represent the number of dice
#And hiding them, to let them appear on the screen later
one = turtle.Turtle()
one.hideturtle()
two = turtle.Turtle()
two.hideturtle()
three = turtle.Turtle()
three.hideturtle()
four = turtle.Turtle()
four.hideturtle()
five = turtle.Turtle()
five.hideturtle()
six = turtle.Turtle()
six.hideturtle()

sc.setup(1000, 1000)

#Creating a list of turtles and images to represent the turtles
turtles = [one, two, three, four, five, six]
images = ['one.gif', 'two.gif', 'three.gif', 'four.gif', 'five.gif', 'six.gif']

#Adding images of dice to the shapes python can be represented with
for image in images:
	sc.addshape(name = image, shape = None)

#Getting the number of times the user wants to play
rounds = sc.numinput("DICEY SUMS", "To win try to get more than 80 percent\nof the rounds\nHow many rounds? ")
 
#Possible points of turtles stored in a dictionary
pp = { -200 : 250, 50 : 250, 300 : 250, -250 : -250, 0 : -250, 250 : -250}

keys = pp.keys()
keys = list(keys)

#i = 0
#total = 0
#points = 0

def play_game(i, total, points):
	while(i < rounds):
		number_die = random.randint(2, 5)
		#Setting a timer for the number of seconds you have to add
		if number_die == 2:
			my_timer = 1
		elif number_die == 3:
			my_timer = 2
		elif number_die == 4:
			my_timer = 3
		elif number_die == 5:
			my_timer = 4

		#Based on the random number generated, we created a list of the turtles used
		turtle_used = turtles[0: number_die]
		#Randomly assigning a dice to a turtle
		images_false = images[:]
		# Randomly giving each turtle a die image
		# Assigning each turtle used a value based on their die image, and adding them to get the sum
		for t in turtle_used:
			shape = random.choice(images_false)
			if shape == "one.gif":
				val = 1
				total += val
			elif shape == "two.gif":
				val = 2
				total += val
			elif shape == "three.gif":
				val = 3
				total += val
			elif shape == "four.gif":
				val = 4
				total += val
			elif shape == "five.gif":
				val = 5
				total += val
			else:
				val = 6
				total += val
			t.shape(shape)
			images_false.remove(shape)

		#Randomly placing a used turtle onto the screen
		keys_false = keys[:]
		for t in turtle_used:
			t.hideturtle()
			x_cor = random.choice(keys_false)
			t.up()
			t.goto(x_cor, pp[x_cor])
			t.showturtle()
			keys_false.remove(x_cor)

	# Starting timer after turtles have been placed
	# And clearing the screen when the timer is out
	# After clearing the screen ask user for input
		while my_timer > 0:
				sleep(1)
				my_timer -= 1
		if my_timer == 0:
			for t in turtle_used:
				t.hideturtle()
			sum = sc.numinput("DICEY SUMS", f"Points: {points}\nClick 'cancel' to exit\nWhat is the sum: ")
			sum = int(sum)

			if sum == total:
				points += 1
				os.system("afplay correct.wav&")
			else:
				os.system("afplay lose.wav&")
		total = 0
		i = i + 1
	
	percent = (points / rounds) * 100

	if percent >= 80:
		message = "You Won!"
	else:
		message = "You lost"
	dialogue_box = sc.textinput("DICEY SUMS", f" {message}\nWould you like to play again? Yes or no")
	return dialogue_box

play_game(0, 0, 0)



if  play_game(0, 0, 0) == "Yes":
	play_game(0, 0, 0)
else:
	turtle.done()