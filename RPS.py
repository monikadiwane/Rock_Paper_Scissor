#hand gesture for rock, paper and scissor
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

#import libraries
import random

while(1):
    #take user input
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    if user_input < 0 or user_input > 2:
        print("Wrong choice entered. Please enter the correct choice again.")
        continue
    else:
        break

game_images = [rock, paper, scissors]

#print user choice
print(game_images[user_input])
        
computer_chose = random.randint(0,2)
#print computer choice
print("Computer chose:")
print(game_images[computer_chose])
    

if user_input == computer_chose:
    print("It's a tie")
elif user_input == 0 and computer_chose == 2:
    print("You Win")
elif user_input == 2 and computer_chose == 0:
    print("You Loose")
elif user_input < computer_chose:
    print("You Loose")
else:
    print("You Win")
