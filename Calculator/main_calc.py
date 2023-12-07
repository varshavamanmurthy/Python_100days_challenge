from art import logo
from replit import clear
from calculation import  add, sub, mul, div

print(logo)
calc_dict = {
              '+': add, 
              '-': sub,
              '*': mul,
              '/': div
            }


def calculator():
  
  num1 = float(input("What's the first number?: "))
  for symbol in calc_dict:
    print(symbol)
  is_continue = True
  
  while is_continue:
      operator = input("Pick an operation from the above lines: ")
      num2 = float(input("What's the next number?: "))
      func = calc_dict[operator]
      answer = func(num1, num2)
      print(f"{num1} {operator} {num2} = {answer}")
      continue_question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

      if continue_question=='y':
        num1 = answer

      elif continue_question =='n':
        is_continue = False
        calculator()

calculator()



