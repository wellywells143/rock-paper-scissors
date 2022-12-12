# This code has been created by user DJWang
# Original code from: https://replit.com/talk/share/Rock-Paper-Scissors/20693

# This mimics Rock, Paper, Scissors but in Python!
# Play around with this program & study the code on your own
# For more info on creating this game on your own, read this:
# https://realpython.com/python-rock-paper-scissors/

# NOTE: This is not this week's exit ticket.

import random
ScoreAi = 0
ScorePlayer = 0
while True:
  print('Hi player one, You can either be')
  print('1) Rock')
  print('2) Paper')
  print('3) Scissors')
  PlayerOne = int(input('Pick 1, 2, or 3. '))
  Computer = random.randint(1,3)
  print('The Computer chose ' + str(Computer))
  if PlayerOne == Computer:
    print('It is a tie!')
    ScoreAi = ScoreAi + 1
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 1 and Computer == 2:
    print(' Computers Paper beats your rock! You lose! ')
    ScoreAi = ScoreAi + 1
  elif PlayerOne == 1 and Computer == 3:
    print('Your Rock beats Computers scissors! You win!')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 2 and Computer == 3:
    print('Computers Scissors beats your paper! You Lose!')
    ScoreAi = ScoreAi + 1
  elif PlayerOne == 2 and Computer == 1:
    print('Your Paper beats Computers rock! You Win!')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 3 and Computer == 2:
    print('Your Scissors beats Computers paper! You Win!')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 3 and Computer == 1:
    print('Computers Rock beats your paper! You Lose!')
    ScoreAi = ScoreAi + 1
  print('Do you want to keep playing?')
  print('1) Yes')
  print('2) No')
  Choice = input('Choose 1 or 2.')

  if Choice == '2':
    print('You won ' + str(ScorePlayer) + ' games and the computer won ' + str(ScoreAi) + ' games.')
    if ScorePlayer > ScoreAi:
      print('Congratulations! You win!')
    elif ScorePlayer < ScoreAi:
      print('The computer won most of the games. You lose!')
    else:
      print('Tie!')
    print('Thank you for playing!')
    break
import random

user_action = input("Will you pick rock, paper, or scissors?:")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
# print(computer_action)
print(f"You chose: {user_action} , Computer chose: {computer_action}")

if user_action == computer_action:
  print("It's a tie!")
elif user_action == "paper":
  if computer_action == "rock":
    print("Paper covers Rock. User Wins!")
elif user_action == "scissors":
  if computer_action == "paper":
    print("Scissors cuts paper! User Wins!")
elif user_action == "rock":
  if computer_action == "scissors":

 import random

user_action = input("Will you pick rock, paper, or scissors?:")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
# print(computer_action)
print(f"You chose: {user_action} , Computer chose: {computer_action}")

if user_action == computer_action:
  print("It's a tie!")
elif user_action == "paper":
  if computer_action == "rock":
    print("Paper covers Rock. User Wins!")
  else:
    print("Scissors cuts paper! Computer Wins!")
elif user_action == "scissors":
  if computer_action == "paper":
    print("Scissors cuts paper! User Wins!")
  else:
    print("Rock smashes scissors! Computer Wins!")
elif user_action == "rock":
  if computer_action == "scissors":
    print("Rock smashes Scissors. User Wins!")
  else:
    print("Paper covers rock! Computer Wins!")
   