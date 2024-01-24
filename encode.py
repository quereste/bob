import torch

def cardsToOneHot(cards):
  outcome = torch.zeros(52)

  outcome[cards] = 1
  return outcome

def allowedCards(cards, firstPlayedCard):
  cards = cardsToOneHot(cards)

  if firstPlayedCard == -1:
    return cards

  suit = firstPlayedCard // 13
  mask = torch.zeros(52)
  mask[13*suit:(13*(suit+1))] = 1

  outcome = cards * mask
  outcome_sum = outcome.sum()

  if outcome_sum > 0:
    return outcome
  return cards

def triumphToOneHot(triumph):
  triumphs = torch.zeros(5)
  triumphs[triumph] = 1
  return triumphs