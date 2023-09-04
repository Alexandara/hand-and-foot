import pytest
import sys
sys.path.append("../hand_and_foot")

from hand_and_foot.game_objects import Suits, Card, FiveDecks, Discard

def test_five_decks():
	deck_ordered = FiveDecks()
	deck_shuffled = FiveDecks()
	deck_shuffled.shuffle()
	deck_small = FiveDecks(decks=1)
	assert deck_ordered.length() == 270
	assert deck_shuffled.length() == 270
	assert deck_small.length() == 54
	assert deck_ordered.cards != deck_shuffled.cards
	deck_small.deal()
	assert deck_small.length() == 53

def test_discard():
	discard_pile = Discard()
	assert len(discard_pile.cards) == 0
	discard_pile.add(Card(Suits.SPADE, 3))
	assert len(discard_pile.cards) == 1
	five_cards_peek = discard_pile.peek()
	assert len(five_cards_peek) == 1
	assert len(discard_pile.cards) == 1
	five_cards_draw = discard_pile.draw()
	assert len(five_cards_draw) == 1
	assert len(discard_pile.cards) == 0
	assert five_cards_draw[0].suit == Suits.SPADE
	assert five_cards_draw[0].value == 3
	discard_pile.add(Card(Suits.SPADE, 1))
	discard_pile.add(Card(Suits.SPADE, 2))
	discard_pile.add(Card(Suits.SPADE, 3))
	discard_pile.add(Card(Suits.SPADE, 4))
	discard_pile.add(Card(Suits.SPADE, 5))
	assert len(discard_pile.cards) == 5
	five_cards_draw = discard_pile.draw()
	assert len(five_cards_draw) == 5
	assert len(discard_pile.cards) == 0
	discard_pile.add(Card(Suits.SPADE, 1))
	discard_pile.add(Card(Suits.SPADE, 2))
	discard_pile.add(Card(Suits.SPADE, 3))
	discard_pile.add(Card(Suits.SPADE, 4))
	discard_pile.add(Card(Suits.SPADE, 5))
	discard_pile.add(Card(Suits.SPADE, 6))
	five_cards_peek = discard_pile.peek()
	assert len(five_cards_peek) == 5
	assert len(discard_pile.cards) == 6
	five_cards_draw = discard_pile.draw()
	assert len(five_cards_draw) == 5
	assert len(discard_pile.cards) == 1
