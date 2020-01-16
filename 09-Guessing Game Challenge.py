#!/usr/bin/env python
# coding: utf-8

# # Guessing Game Challenge
# 
# Let's use `while` loops to create a guessing game.
# 
# The Challenge:
# 
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# 
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
#  * within 10 of the number, return "WARM!"
#  * further than 10 away from the number, return "COLD!"
# 3. On all subsequent turns, if a guess is 
#  * closer to the number than the previous guess return "WARMER!"
#  * farther from the number than the previous guess, return "COLDER!"
# 4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!
# 
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
# 

# #### First, pick a random integer from 1 to 100 using the random module and assign it to a variable
# 
# Note: `random.randint(a,b)` returns a random integer in range `[a, b]`, including both end points.

# In[2]:


from random import randint
random_num = randint(1,100)
#print(random_num)
player_guess = int(input("Enter guess from 1 to 100: "))
previous_guess = 0
turn = 1

while player_guess != random_num:
    if player_guess <1 or player_guess > 100:
        print('OUT OF BOUNDS')
    if turn == 1:
        if abs(player_guess - random_num) == 10:
            print("WARM!")
        else:
            print("COLD!")
    if turn > 1:
        if abs(previous_guess - random_num) > abs (player_guess - random_num):
            print("WARMER!")
        else:
            print("COLDER!")
    
    previous_guess = player_guess
    player_guess = int(input("new guess: "))
    turn += 1
    
print('You have guessed correctly', random_num, '. it took you', turn, ' guess(es)')





# That's it! You've just programmed your first game!
# 
# In the next section we'll learn how to turn some of these repetitive actions into *functions* that can be called whenever we need them.

# ### Good Job!
