"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
"""
__author__ = 'kris'


if __name__ == '__main__':

  game = "y"
  while (game=="y"):
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
    if player1 == "s":
      if player2 =="r":
        print("player two wins")
      elif player2 == "p":
        print("Player one wins")
      else:
        print("equals")
    if player1 == "p":
      if player2 =="r":
        print("player one wins")
      elif player2 == "p":
        print("equals")
      else:
        print("player one wins")
    game = raw_input("game agayn?")
