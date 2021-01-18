#import
import random
#Introduction
def game():
  print("Welcome to guess a number game")
  print("I am thinking of a number betwwen 1 and 100")
  #computer guess a number
  computer_guess = random.randint(1,100)
  print(computer_guess)


  #choosing a difficulty level
  level = input("Choose a difficulty: Type 'easy' or 'hard':  ")



  if level == 'easy':
    life = 10
  elif level == 'hard':
    life = 5
    
  while life > 0:
    print(f"You have {life} attempt remaining to guess the number")
    guess = int(input("Make a guess: "))

    if guess == computer_guess:
      print("You Win")
      life = 0
    elif guess > computer_guess:
      print("Too High\n Guess again.")
      
      life -= 1
      if life == 0:
        print("You dont have any more attempt")
    else:
      print("Too Low\n Guess again.")
      life -= 1
      if life == 0:
        print("You dont have any more attempt")
  start = input("Would you like to play again? Type 'y' to play or 'n' to stop")
  if start == 'y':
    game()

      
    
game()