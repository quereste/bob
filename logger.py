def printTriumph(triumph):
  if triumph == 4:
    print("NT")
  elif triumph == 3:
    print("spades")
  elif triumph == 2:
    print("hearts")
  elif triumph == 1:
    print("diamonds")
  elif triumph == 0:
    print("clubs")

def printCards(cards):
  for card in cards:
    figure = card % 13
    if figure >= 0 and figure <= 8:
      print(f"{figure + 2}(#{card})", end="")
    elif figure == 9:
      print(f"J(#{card})", end="")
    elif figure == 10:
      print(f"D(#{card})", end="")
    elif figure == 11:
      print(f"K(#{card})", end="")
    else:
      print(f"A(#{card})", end="")


def printHand(cards):

  spades = filter(lambda c: c >= 39, cards)
  hearts = filter(lambda c: c >= 26 and c < 39, cards)
  diamonds = filter(lambda c: c >= 13 and c < 26, cards)
  clubs = filter(lambda c: c >= 0 and c < 13, cards)
  print("spades: ", end="")
  printCards(spades)
  print(" hearts: ", end="")
  printCards(hearts)
  print(" diamonds: ", end="")
  printCards(diamonds)
  print(" clubs: ", end="")
  printCards(clubs)
  print()