import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """
    This is a deck of cards class
    
    A single element of the class:
    >>> beer_card = Card('7', 'diamonds')
    >>> beer_card
    Card(rank='7', suit='diamonds')

    Intializing the deck:
    >>> deck = FrenchDeck()
    >>> len(deck) 
    52

    Getting the first and last element of the deck:
    >>> deck[0]  
    Card(rank='2', suit='spades')
    >>> deck[-1] 
    Card(rank='A', suit='hearts')
    
    Getting a random card in the deck:
    >>> from random import choice
    >>> choice(deck)
    Card(rank='3', suit='hearts')
    >>> choice(deck)
    Card(rank='K', suit='spades')
    >>> choice(deck)
    Card(rank='2', suit='clubs')

    Indexing into the deck:
    >>> deck[:3]
    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    >>> deck[12::13]
    [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

    Iterating through the deck of cards
    >>> for card in deck: # doctest: +ELLIPSIS
    ...   print(card)
    Card(rank='2', suit='spades')
    Card(rank='3', suit='spades')
    Card(rank='4', suit='spades')
    ...
    
    Iterating through the deck of cards in reverse
    >>> for card in reversed(deck): # doctest: +ELLIPSIS
    ...   print(card)
    Card(rank='A', suit='hearts')
    Card(rank='K', suit='hearts')
    Card(rank='Q', suit='hearts')
    ...

    Checking if a card is in a deck
    >>> Card('Q', 'hearts') in deck
    True
    >>> Card('7', 'beasts') in deck
    False
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
