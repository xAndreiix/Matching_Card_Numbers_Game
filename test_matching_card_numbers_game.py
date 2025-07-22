import unittest
import matching_card_numbers_game as game


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card1 = game.Card(5, 0, 0)
        self.card2 = game.Card(5, 0, 0)
        self.card3 = game.Card(3, 0, 0)

    def test_initial_state(self):
        self.assertFalse(self.card1.is_flipped)
        self.assertFalse(self.card1.is_matched)

    def test_flip_card(self):
        self.card1.is_flipped = True
        self.assertTrue(self.card1.is_flipped)

    def test_matching_cards(self):
        self.assertEqual(self.card1.value, self.card2.value)
        self.card1.is_matched = True
        self.card2.is_matched = True
        self.assertTrue(self.card1.is_matched)
        self.assertTrue(self.card2.is_matched)

    def test_non_matching_cards(self):
        self.assertNotEqual(self.card1.value, self.card3.value)

    def test_create_cards_pairing(self):
        cards = game.create_cards()
        values = [card.value for card in cards]
        for val in set(values):
            self.assertEqual(values.count(val), 2)

    def test_win_condition(self):
        cards = game.create_cards()
        for card in cards:
            card.is_matched = True
        self.assertTrue(all(c.is_matched for c in cards))

if __name__ == "__main__":
    unittest.main()
