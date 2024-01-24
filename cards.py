import random

def deal_cards():
  a = [*range(52)]
  random.shuffle(a)
  outcome = [a[:13], a[13:26], a[26:39], a[39:]]
  for hand in outcome:
    hand.sort()
    hand.reverse()

  return outcome

def findWinner(playedCards, triumph):
  suit_played = playedCards[0] // 13

  if triumph == 4:
    winner = 0
    for i in range(1,4):
      if playedCards[i] // 13 == suit_played and playedCards[i] > playedCards [winner]:
        winner = i
    return winner
  winner = -1

  for i in range (0,4):
    if playedCards[i] // 13 == triumph and (winner == -1 or playedCards[i] > playedCards [winner]):
      winner = i

  if winner != -1:
    return winner

  winner = 0
  for i in range(1,4):
    if playedCards[i] // 13 == suit_played and playedCards[i] > playedCards [winner]:
      winner = i
  return winner

def find_player(whoPlays):
  if whoPlays == 0:
    return 'W'
  elif whoPlays == 1:
    return 'N'
  elif whoPlays == 2:
    return 'E'
  elif whoPlays == 3:
    return 'S'
  raise Exception("Unrecognized site passed: find_player")  
