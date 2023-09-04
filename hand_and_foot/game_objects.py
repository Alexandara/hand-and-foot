from enum import Enum
import pygame
import random


class Suits(Enum):
    CLUB = 0
    SPADE = 1
    HEART = 2
    DIAMOND = 3
    JOKER = 4


class Card:
    suit = None
    value = None
    image = None

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load('../images/' + self.suit.name + '-' + str(self.value) + '.svg')


class FiveDecks:
    cards = None

    def __init__(self, decks=5):
        self.cards = []
        for _ in range(decks):
            for suit in Suits:
                if suit == Suits.JOKER:
                    self.cards.append(Card(suit, 1))
                    self.cards.append(Card(suit, 2))
                else:
                    for value in range(1, 14):
                        self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def length(self):
        return len(self.cards)


class Discard:
    cards = None

    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def peek(self):
        top_five_cards = []
        if (len(self.cards) > 0):
            top_five_cards.append(self.cards[-1])
        if (len(self.cards) > 1):
            top_five_cards.append(self.cards[-2])
        if (len(self.cards) > 2):
            top_five_cards.append(self.cards[-3])
        if (len(self.cards) > 3):
            top_five_cards.append(self.cards[-4])
        if (len(self.cards) > 4):
            top_five_cards.append(self.cards[-5])
        return top_five_cards

    def popAll(self):
        return self.cards

    def clear(self):
        self.cards = []

    def draw(self):
        top_five_cards = []
        while len(top_five_cards) < 5 and len(self.cards) > 0:
            top_five_cards.append(self.cards.pop())
        return top_five_cards