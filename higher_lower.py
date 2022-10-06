#imports art, game data and random module
from art import logo, vs
from game_data import data
from random import choice 

#prints two options and returns option_b
def present_choices(option_a):
  print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
  print(vs)
  option_b = choice(data)
  print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
  return option_b

def game():
  #picks an A option randomly to start the game and sets starting score to 0
  score = 0
  option_a = choice(data)

  #starts a while loop to repeat as long as winning = True
  winning = True
  while winning:
    #prints choices, feeding in option A and generating a new option B
    option_b = present_choices(option_a)
    
    #asks for a choice between a and b  
    pick = input("Who has more followers? Type 'A' or 'B': ").lower()  

    #evaluates if choice is right or wrong, updates score and makes the winner the new a
    if pick == "a" and option_a['follower_count'] > option_b['follower_count']:
      score += 1 
      print(f"You're right! Current score: {score}")
    elif option_b['follower_count'] > option_a['follower_count'] and pick == "b":
      score += 1     
      print(f"You're right! Current score: {score}") 
      option_a = option_b
    else: 
      winning = False
    

  print(f"Sorry, that's wrong. Final score: {score}")



game()
  
