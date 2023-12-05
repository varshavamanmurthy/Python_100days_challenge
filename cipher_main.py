alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
import re

print(logo)
#end_or_continue = input("Do you restart cipher program ? Type 'yes' or 'No': ").lower()


def caesar(msg_text, shift_amt, direction_path):
      result = ''
      for letter in msg_text:
        if letter in alphabet:
          position = alphabet.index(letter)
          new_shift = shift_amt % 26
          if direction_path == 'encode':
            new_position = position + new_shift
          elif direction_path == 'decode':
              new_position = position - new_shift
          result+=alphabet[new_position]
        #if number or symbol or ' '
        else:
            result+=letter

      print(f"The {direction_path}d text is {result}")



continue_prog = True
while continue_prog:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction in ('encode', 'decode'):
      
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      #Function call
      caesar(msg_text = text, shift_amt = shift, direction_path=direction)
      continue_prog = input("Do you restart cipher program ? Type 'yes' or 'No': ").lower()
    
      if continue_prog == 'yes':
        continue
      elif continue_prog == 'no':
        break
    else:
      print(f"Please type 'encode' or 'decode' only")
print('Thank you for using cipher program')
    