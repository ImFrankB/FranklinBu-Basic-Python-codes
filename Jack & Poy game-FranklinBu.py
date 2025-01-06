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

scissor = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''


game_images = [rock, scissor, paper]

print ("welcome to Jack em poy")
       
user_choice = int(input("Choose 0 for rock, 1 for scissors, 2 for paper \n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print ("Computer chose: \n")
print(game_images[computer_choice])
    
    
if user_choice>=3  or  computer_choice<0:
    print("you entered a invalid number, you lose ")
else:

    if computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif user_choice ==1 and computer_choice == 0:
        print("you win")
    elif computer_choice==1 and user_choice ==0:
        print("You lose")
    elif computer_choice == 1 and user_choice ==2:
        print("You lose!")
    elif user_choice == 1 and computer_choice ==2:
        print("You win!")
    elif computer_choice == 0 and user_choice ==1:
        print("You lose!")
    elif user_choice == 0 and computer_choice ==1 :
        print("You win!")
    elif computer_choice == 1 and user_choice ==2:
        print("You lose!")
    elif user_choice == 1 and computer_choice ==2 :
        print("You win!")
    else:
        print("draw! ")
