alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

if direction != 'encode' and direction != 'decode':
    print("Invalid input. Please type 'encode' or 'decode'.")

text = input("Type your message:\n").lower()
    
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
      cipher_text = ""
      for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position > 25:
            new_position -= 26
        cipher_text += alphabet[new_position]

        if letter == text[-1]:
          print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
      decipher_text = ""
      for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        if new_position < 0:
            new_position += 26
        decipher_text += alphabet[new_position]

        if letter == text[-1]:
          print(f"The decoded text is {decipher_text}")

if direction == 'encode':
   encrypt(text, shift)
   
if direction == 'decode':
   decrypt(text, shift)

question=input("Want to encrypt or decrypt again? Type 'yes' or 'no':\n").lower()

if question == 'yes':
     choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
     text = input("Type your message:\n").lower()
     shift = int(input("Type the shift number:\n"))

     if choice == 'encode':
        encrypt(text, shift)
    
     elif choice == 'decode':
         decrypt(text, shift)

else:
    print("Goodbye!")