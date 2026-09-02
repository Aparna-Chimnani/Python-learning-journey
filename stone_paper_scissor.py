import random


user_choice= int(input("What is your choice , 0, 1 or 2?"))

computer_choice= random.randint(0,2)

game=[ 'rock', 'paper', 'scissor']
print(f'Computer choosed {game[computer_choice]}')
print(f'user choosed {game[user_choice]}')

if user_choice < 0 and user_choice > 2:
    print('Invalid Choice')

elif user_choice == computer_choice:
    print("draw")

elif user_choice == 0 and computer_choice == 1:
    print('Computer wins')

elif user_choice == 0 and computer_choice == 2:
    print('user wins')

elif user_choice == 1 and computer_choice == 0:
    print('user wins')

elif user_choice == 1 and computer_choice == 2:
    print('computer wins')

elif user_choice == 2 and computer_choice == 0:
    print('computer wins')

elif user_choice == 2 and computer_choice == 1:
    print('user wins')
                 