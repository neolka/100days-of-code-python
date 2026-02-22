import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors : "))
if userChoice >= 0 and userChoice <= 2:
    print("User choice: ")
    print(game_images[userChoice])

computerChoice = random.randint(0,2)
print("Computer choice: ")
print(game_images[computerChoice])

'''Rock beats scissors, scissors beats paper, and paper beats rock. '''

if userChoice > 2 or userChoice < 0:
    print ("You entered wrong choice. Please try again.")
elif userChoice == computerChoice:
    print("It is a draw! You can try again.")
elif userChoice == 0 and computerChoice == 2:
    print ("You win!")
elif userChoice == 2 and computerChoice == 0:
    print("You lose!")
elif userChoice > computerChoice:
    print("You win!")
elif computerChoice > userChoice:
    print("You lose!")
else:
    print("Looks like you entered incorrect value. Please try again.")
