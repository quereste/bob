from cards import deal_cards, findWinner
from model import Bob, saveBob
from encode import cardsToOneHot, allowedCards, triumphToOneHot
from loss_function import SzczepanikLoss

import torch

def train(num_of_games = 100000, save_path = './save/model_100000.pth'):

    bob = Bob()
    loss_fn = SzczepanikLoss()

    for game_num in range(num_of_games):
        cards = deal_cards()
        whoPlays = 0 # W - 0, N - 1, E - 2, S - 3
        triumph = 4
        ns_points = 0

        eval = []

        for trick_num in range(13):
            played_cards = []

            for i in range(4):
                current_player = (whoPlays + i) % 4
                next_player = (current_player + 1) % 4
                next_next_player = (current_player + 2) % 4
                next_next_next_player = (current_player + 3) % 4

                played_scores = bob.forward(
                    torch.cat((cardsToOneHot(cards[current_player]),
                                allowedCards(cards[current_player], -1),
                                cardsToOneHot(played_cards),
                                cardsToOneHot(cards[next_player]),
                                cardsToOneHot(cards[next_next_player]),
                                cardsToOneHot(cards[next_next_next_player]),
                                triumphToOneHot(triumph))))

                played_cards.append(int(torch.argmax(played_scores)))
                cards[current_player].remove(played_cards[i])

                eval.append([played_scores, current_player])

            whoPlays = (whoPlays + findWinner(played_cards, triumph)) % 4
            if whoPlays % 2 == 1:
                ns_points += 1


        for output, side in eval:
            if (side%2 == 0):
                loss = loss_fn(output, 13 - ns_points)
                loss.backward()
            else:
                loss = loss_fn(output, ns_points)
                loss.backward()

        if game_num % 100 == 0:
            print("Training game number: ", game_num)

    if save_path is not None:
        saveBob(bob, save_path)

train(1000)