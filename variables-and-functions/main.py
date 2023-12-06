import random
# create variables

# player_choice = "rock"
# computer_choice = "paper"

# create functions

def get_choices():
  # player_choice = "rock"
  # computer_choice = "paper"
  
  # choices = { "player": player_choice, "computer": computer_choice }
  
  # return choices
  options = ["rock", "paper", "scissors"]
  player_choice = input("Please choose rock, paper, or scissors: ")
  computer_choice = random.choice(options)
  
  choices = { "player": player_choice, "computer": computer_choice }
  
  return choices

def check_win(player, computer):
  print(f"you chose: {player}, computer chose: {computer}")

  if player == computer:
    return "It's a tie"
  elif player == "rock" and computer == "paper":
    return "You lose"
  elif player == "rock" and computer == "scissors":
    return "You win"
  elif player == "paper" and computer == "rock":
    return "You win"
  elif player == "paper" and computer == "scissors":
    return "You lose"
  elif player == "scissors" and computer == "rock":
    return "You lose"
  elif player == "scissors" and computer == "paper":
    return "You lose"
  

# def greeting():
#   return "Hi :)"

check_win("rock", "paper")
print(get_choices())
# response = greeting()
# print(response)

# dictionary
dict = {"name": "beau", "color": "blue"}

