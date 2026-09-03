import random

print("Welcome to the Hangman game!")

words= ['programming', 'python', 'hangman', 'computer']

word= random.choice(words)
print(f"The word is: {word}")

count = len(word)

blank = '_' * len(word)
print(blank)


letter=[]
Game_won = False

while(not Game_won):

 display =''

 guess= input("Guess a letter: ")
 for char in word:
    if char == guess:
        display += char
        letter.append(guess)

    elif char in letter:
        display += char

    elif char != guess:
        display += '_'

 if guess not in word:
        count -= 1 
        if count > 0:
           print(f"You have {count} chances left")

        if count == 0:
            print("You lost the game!")
            break       

    
 print(display)

 if display == word:
    Game_won = True
    print("You won the game!")

          


 


