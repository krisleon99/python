"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
"""
__author__ = 'kris'


if __name__ == '__main__':
  print("Rocks = r")
  print("Scissors = s")
  print("Paper = p")
  player1 = raw_input("player one says:")
  player2 = raw_input("payer two says;")

  if player1 == "r":
    if player2 =="r":
      print("equals")
    elif player2 == "p":
      print("Player two wins")
    else:
      print("player one wins")

  a = 5
  while (a>0):
    print(a)
    a -= 1
