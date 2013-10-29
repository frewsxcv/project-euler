from collections import Counter
from functools import total_ordering


@total_ordering
class Hand():

    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

    def __init__(self, hand_list):
        self.cards = map(Card, hand_list)
        self.suites = [card.suite for card in self.cards]
        self.values = sorted(card.value for card in self.cards)
        self._counter = Counter(self.values)
        self.best_hand = self._best_hand()

    def _best_hand(self):
        if self.has_straight() and self.has_flush():
            return self.STRAIGHT_FLUSH
        if self.has_four_of_a_kind():
            return self.FOUR_OF_A_KIND
        if self.has_full_house():
            return self.FULL_HOUSE
        if self.has_flush():
            return self.FLUSH
        if self.has_straight():
            return self.STRAIGHT
        if self.has_three_of_a_kind():
            return self.THREE_OF_A_KIND
        if self.has_two_pairs():
            return self.TWO_PAIRS
        if self.has_one_pair():
            return self.ONE_PAIR
        return self.HIGH_CARD

    def ranked_values(self):
        (x, _), (y, _) = self._counter.most_common(2)
        if self.best_hand == self.FOUR_OF_A_KIND:
            return [x] * 4 + [y]
        if self.best_hand == self.FULL_HOUSE:
            return [x] * 3 + [y] * 2
        if self.best_hand == self.THREE_OF_A_KIND:
            rest = sorted(set(self.values) - {x}, reverse=True)
            return [x] * 3 + rest
        if self.best_hand == self.TWO_PAIRS:
            rest = sorted(set(self.values) - {x, y}, reverse=True)
            return ([x] * 2 + [y] * 2 if x > y else [y] * 2 + [x] * 2) + rest
        if self.best_hand == self.ONE_PAIR:
            rest = sorted(set(self.values) - {x}, reverse=True)
            return [x] * 2 + rest
        return self.values[::-1]

    def has_two_pairs(self):
        most_common, second_most = self._counter.most_common(2)
        return most_common[1] == 2 and second_most[1] == 2

    def has_four_of_a_kind(self):
        most_common, = self._counter.most_common(1)
        return most_common[1] == 4

    def has_three_of_a_kind(self):
        most_common, = self._counter.most_common(1)
        return most_common[1] == 3

    def has_one_pair(self):
        most_common, = self._counter.most_common(1)
        return most_common[1] == 2

    def has_full_house(self):
        most_common, second_most = self._counter.most_common(2)
        return most_common[1] == 3 and second_most[1] == 2

    def has_straight(self):
        # Note: Does not count A,2,3,4,5 as a straight
        min_card = min(self.values)
        return self.values == range(min_card, min_card+5)

    def has_flush(self):
        return len(set(self.suites)) == 1

    def __lt__(self, other):
        if self.best_hand == other.best_hand:
            return self.ranked_values() < other.ranked_values()
        return self.best_hand < other.best_hand


class Card():
    def __init__(self, card_str):
        self.value = self._num_value(card_str[0])
        self.suite = card_str[1]

    @staticmethod
    def _num_value(value):
        if value == "A":
            return 14
        if value == "K":
            return 13
        if value == "Q":
            return 12
        if value == "J":
            return 11
        if value == "T":
            return 10
        return int(value)


if __name__ == "__main__":

    with open("poker.txt") as input_fp:
        input_lines = (line.strip() for line in input_fp.readlines())

    player1_wins = 0

    for line in input_lines:
        line = line.split()
        player1_hand = Hand(line[:5])
        player2_hand = Hand(line[5:])

        if player1_hand > player2_hand:
            player1_wins += 1

    print player1_wins
