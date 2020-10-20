from random import shuffle

PlayerChoice = ''


class _card:
    def __init__(self, _rank, _suit):
        self.Rank = _rank
        self.Suit = _suit


class _player:
    def __init__(self):
        self.Hand = []
        self.Score = 0


Player = _player()
Dealer = _player()
Suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
Ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
Shoe = []
Deck = []
EndGame = False

for Suit in Suits:
    for Rank in Ranks:
        Card = _card(Rank, Suit)
        Deck.append(Card)

shuffle(Deck)

for x in range(6):
    for Card in Deck:
        Shoe.append(Carhd)

shuffle(Shoe)
Deck = []

while not EndGame and len(Shoe) >= 10:
    Player.Score = 0
    Dealer.Score = 0
    Player.Hand = []
    Dealer.Hand = []

    for x in range(2):
        PlayerCard = Shoe.pop()
        DealerCard = Shoe.pop()
        Player.Hand.append(PlayerCard)
        Dealer.Hand.append(DealerCard)

    for Card in Player.Hand:
        if Card.Rank not in ['J', 'Q', 'K', ] and Card.Rank != 'A':
            Player.Score += Card.Rank

        elif Card.Rank in ['J', 'Q', 'K', ]:
            Player.Score += 10

        elif Card.Rank == 'A':
            if Player.Score >= 11:
                Player.Score += 1

            else:
                Player.Score += 11

    for Card in Dealer.Hand:
        if Card.Rank not in ['J', 'Q', 'K', ] and Card.Rank != 'A':
            Dealer.Score += Card.Rank

        elif Card.Rank in ['J', 'Q', 'K', ]:
            Dealer.Score += 10

        elif Card.Rank == 'A':
            if Dealer.Score >= 11:
                Dealer.Score += 1

            else:
                Dealer.Score += 11

    while Player.Score < 21 and Dealer.Score < 21:
        for Card in Player.Hand:
            print(Card.Rank, "of", Card.Suit)

        print("Your Hand Score =", Player.Score)
        PlayerChoice = input("Hit or Stay? ('H' = Hit, 'S' = Stay, 'Q' = Quit): ")

        if PlayerChoice in ['h', 'H']:
            print("Hit")
            Card = Shoe.pop()

            if Card.Rank not in ['J', 'Q', 'K', ] and Card.Rank != 'A':
                Player.Score += Card.Rank

            elif Card.Rank in ['J', 'Q', 'K', ]:
                Player.Score += 10

            elif Card.Rank == 'A':
                if Player.Score >= 11:
                    Player.Score += 1

                else:
                    Player.Score += 11
            print()

            Player.Hand.append(Card)

        elif PlayerChoice in ['s', 'S']:
            print("Stay")
            break

        elif PlayerChoice in ['q', 'Q']:
            EndGame = True
            break

        else:
            print()

    while Dealer.Score < 17:
        Card = Shoe.pop()

        if Card.Rank not in ['J', 'Q', 'K', ] and Card.Rank != 'A':
            Dealer.Score += Card.Rank

        elif Card.Rank in ['J', 'Q', 'K', ]:
            Dealer.Score += 10

        elif Card.Rank == 'A':
            if Dealer.Score >= 11:
                Dealer.Score += 1

            else:
                Dealer.Score += 11

        Dealer.Hand.append(Card)

    if PlayerChoice not in ['Q', 'q']:
        if Player.Score == 21:
            print("Winner Winner Chicken Dinner!")

        elif Player.Score > 21:
            print("Rats! You've Busted!")

        elif Dealer.Score == 21:
            print("Dealer Gets Blackjack! Oof.")

        elif Dealer.Score > 21:
            print("Well that sucks. Dealer Busted!")

        else:
            if Player.Score > Dealer.Score:
                print("Whoo Hoo! You've beat the Dealer!")

            elif Player.Score < Dealer.Score:
                print("Well, shucks! He got ya this time!")

            elif Player.Score == Dealer.Score:
                print("Yall tied up! Flip a coin, hud.")

    print()
