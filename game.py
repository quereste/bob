from cards import deal_cards, findWinner, find_player
from logger import printHand, printCards, printTriumph
from model import Bob, loadBob
from encode import cardsToOneHot, allowedCards, triumphToOneHot

import torch

bob = loadBob('./save/bob.pth')

num_of_games = 1
debug_mode = True

for game_num in range(num_of_games):

  cards = deal_cards()
  whoPlays = 0 # W - 0, N - 1, E - 2, S - 3
  triumph = 4
  ns_points = 0

  print("Triumph: ", end="")
  printTriumph(triumph)

  for trick_num in range(13):
    played_cards = []

    if debug_mode:
      print('W:', end="")
      printHand(cards[0])
      print()
    print('N:', end="")
    printHand(cards[1])
    print()
    if debug_mode:
      print('E:', end="")
      printHand(cards[2])
      print()
    print('S:', end="")
    printHand(cards[3])
    print()

    for i in range(4):
      currentPlayer = (whoPlays + i) % 4

      if currentPlayer in [1, 3]:
        print(f"{find_player(currentPlayer)} to play")
        allowedCard = -1
        if len(played_cards) > 0:
          allowedCard = played_cards[0]
        allowed_cards = allowedCards(cards[currentPlayer], allowedCard)
        while True:
          n = int(input('Enter a card: '))
          if n not in cards[currentPlayer]:
            print("You do not posses such card. Try again.")
          elif allowed_cards[n] == 0:
            print("It is illegal to play this card right now. Try again.")
          else:
            played_cards.append(n)
            cards[currentPlayer].remove(n)
            break
      else:
        allowedCard = -1
        if len(played_cards) > 0:
          allowedCard = played_cards[0]
        current_player = (whoPlays + i) % 4
        next_player = (current_player + 1) % 4
        next_next_player = (current_player + 2) % 4
        next_next_next_player = (current_player + 3) % 4

        played_scores = bob.forward(
            torch.cat((cardsToOneHot(cards[current_player]),
                        allowedCards(cards[current_player], allowedCard),
                        cardsToOneHot(played_cards),
                        cardsToOneHot(cards[next_player]),
                        cardsToOneHot(cards[next_next_player]),
                        cardsToOneHot(cards[next_next_next_player]),
                        triumphToOneHot(triumph))))

        played_cards.append(int(torch.argmax(played_scores)))
        cards[currentPlayer].remove(played_cards[i])
      print(f"{find_player(currentPlayer)} played: ", end="")
      printCards([int(played_cards[i])])
      printTriumph(int(played_cards[i]) // 13)
      print("")
    whoPlays = (whoPlays + findWinner(played_cards, triumph)) % 4
    if whoPlays % 2 == 1:
      ns_points += 1
      print("NS took")
    else:
      print("WE took")





