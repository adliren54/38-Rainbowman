myString = input("What sentence do you want rainbow-ising?\n")

def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

for letter in myString:
  if letter.lower() == "r":
    print('\033[31m', end='')
  elif letter.lower() == "b":
    print('\033[34m', end='')
  elif letter.lower() == "g":
    print('\033[32m', end='')
  elif letter.lower() == "p":
    print('\033[35m', end='')
  elif letter.lower() == "y":
    print('\033[33m', end='')
  elif letter == " ":
    print('\033[0m', end='')
    
  print(letter, end="")
  print('\033[0m', end='')