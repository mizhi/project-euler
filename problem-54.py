#!/usr/bin/env python
# In the card game poker, a hand consists of five cards and are
# ranked, from lowest to highest, in the following way:
#
#     * High Card: Highest value card.
#     * One Pair: Two cards of the same value.
#     * Two Pairs: Two different pairs.
#     * Three of a Kind: Three cards of the same value.
#     * Straight: All cards are consecutive values.
#     * Flush: All cards of the same suit.
#     * Full House: Three of a kind and a pair.
#     * Four of a Kind: Four cards of the same value.
#     * Straight Flush: All cards are consecutive values of same suit.
#     * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of
# the highest value wins; for example, a pair of eights beats a pair
# of fives (see example 1 below). But if two ranks tie, for example,
# both players have a pair of queens, then highest cards in each hand
# are compared (see example 4 below); if the highest cards tie then
# the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD          2C 3S 8S 8D TD          Player 2
#               Pair of Fives           Pair of Eights
# 2	 	5D 8C 9S JS AC          2C 5C 7D 8S QH          Player 1
#               Highest card Ace        Highest card Queen
# 3	 	2D 9C AS AH AC          3D 6D 7D TD QD          Player 2
#               Three Aces              Flush with Diamonds
# 4	 	4D 6S 9H QH QC          3D 6D 7H QD QS          Player 1
#               Pair of Queens          Pair of Queens
#               Highest card Nine       Highest card Seven
# 5	 	2H 2D 4C 4D 4S          3C 3D 3S 9S 9D          Player 1
#               Full House              Full House
#               With Three Fours        With Three Threes
#
# The file, poker.txt, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards (separated by a
# single space): the first five are Player 1's cards and the last five
# are Player 2's cards. You can assume that all hands are valid (no
# invalid characters or repeated cards), each player's hand is in no
# specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?
import fileinput

class Card(object):
    card_values = [str(d) for d in xrange(2, 10)]
    card_values.extend(['T', 'J', 'Q', 'K', 'A']);

    def __init__(self, value, suit = None):
        if suit is None:
            self.value = value[0]
            self.suit = value[-1]
        else:
            self.value = value;
            self.suit = suit;

    def num_value(self):
        return Card.card_values.index(self.value)

    def __lt__(self, other):
        return self.num_value() < other.num_value()

    def __le__(self, other):
        return (self < other or self == other)

    def __gt__(self, other):
        return self.num_value() > other.num_value()

    def __ge__(self, other):
        return (self > other or self == other)

    def __eq__(self, other):
        return not (self < other or self > other)

    def __ne__(self, other):
        return not (self == other)

    def __cmp__(self, other):
        if self < other:
            return -1
        elif self == other:
            return 0
        else:
            return 1

    def __str__(self):
        return "%s%s" % (self.value, self.suit)

class Hand(object):
    def __init__(self, card_list):
        self.card_list = card_list
        self.card_list.sort()

    def is_royal_flush(self):        
        return self.is_flush() and self.is_straight() and self.card_list[0].value == 'T'

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_four_of_a_kind(self):
        c_dict = self.count_dict()
        for (c,n) in c_dict.items():
            if len(n) == 4:
                return True
        return False

    def is_full_house(self):
        c_dict = self.count_dict()
        p_count = 0
        t_count = 0
        for (c,n) in c_dict.items():
            if len(n) == 3:
                t_count += 1
            elif len(n) == 2:
                p_count += 1
        return (t_count == 1) and (p_count == 1)

    def is_flush(self):
        return all([x.suit == self.card_list[0].suit for x in self.card_list])

    def is_straight(self):
        return self.card_list[0].num_value() == self.card_list[1].num_value() - 1 and \
            self.card_list[1].num_value() == self.card_list[2].num_value() - 1 and \
            self.card_list[2].num_value() == self.card_list[3].num_value() - 1 and \
            self.card_list[3].num_value() == self.card_list[4].num_value() - 1 

    def is_three_of_a_kind(self):
        c_dict = self.count_dict()
        for (c,n) in c_dict.items():
            if len(n) == 3:
                return True
        return False

    def is_two_pairs(self):
        c_dict = self.count_dict()
        p_count = 0
        for (c,n) in c_dict.items():
            if len(n) == 2:
                p_count += 1
        return (p_count == 2)

    def is_one_pair(self):
        c_dict = self.count_dict()
        p_count = 0
        for (c,n) in c_dict.items():
            if len(n) == 2:
                p_count += 1
        return (p_count == 1)

    def count_dict(self):
        c_dict = {}
        for card in self.card_list:
            if card.num_value() not in c_dict.keys():
                c_dict[card.num_value()] = []
            c_dict[card.num_value()].append(card)
        return c_dict

    def high_card(self):
        return self.card_list[-1]

    def hand_value(self):
        # test for royal flush        
        # test for straight flush
        # test for four of a kind
        # test for full house
        # test for flush
        # test for straight
        # test for three of a kind
        # test for two pairs
        # test for one pair
        # high card    
        if self.is_royal_flush():
            return 10
        elif self.is_straight_flush():
            return 9
        elif self.is_four_of_a_kind():
            return 8
        elif self.is_full_house():
            return 7
        elif self.is_flush():
            return 6
        elif self.is_straight():
            return 5
        elif self.is_three_of_a_kind():
            return 4
        elif self.is_two_pairs():
            return 3
        elif self.is_one_pair():
            return 2
        else:
            return 1

    def __cmp__(self, other):        
        self_value = self.hand_value()
        other_value = other.hand_value()
        if self_value > other_value:
            return 1
        elif self_value < other_value:
            return -1
        else:
            # if the two hands have equal value, then need to get high card
            if self_value == 9: # both had straight flush, get high card
                return cmp(self.card_list[-1], other.card_list[-1])
            elif self_value == 8: # both had four of kind
                # get count dicts for both, find pair cards and cmp them
                c_dict_self = self.count_dict()
                c_dict_other = other.count_dict()
                for (c,n) in c_dict_self.items():
                    if len(n) == 4:
                        self_four = n[0]

                for (c,n) in c_dict_other.items():
                    if len(n) == 4:
                        other_four = n[0]

                return cmp(self_four, other_four)
            elif self_value == 7: # both had full house
                # get count dicts for both, find triple cards and cmp them
                c_dict_self = self.count_dict()
                c_dict_other = other.count_dict()

                for (c,n) in c_dict_self.items():
                    if len(n) == 3:
                        self_t = n[0]

                for (c,n) in c_dict_other.items():
                    if len(n) == 3:
                        other_t = n[0]

                t_cmp = cmp(self_t, other_t)
                return cmp(self.card_list[-1], other.card_list[-1])
            elif self_value == 6: # both had flush
                return cmp(self.card_list[-1], other.card_list[-1])
            elif self_value == 5: # both had straights
                return cmp(self.card_list[-1], other.card_list[-1])
            elif self_value == 4: # both had 3 of kind
                # get count dicts for both, find triple cards and cmp them
                c_dict_self = self.count_dict()
                c_dict_other = other.count_dict()

                for (c,n) in c_dict_self.items():
                    if len(n) == 3:
                        self_t = n[0]

                for (c,n) in c_dict_other.items():
                    if len(n) == 3:
                        other_t = n[0]

                t_cmp = cmp(self_t, other_t)
                if t_cmp == 0:
                    return cmp(self.card_list[-1], other.card_list[-1])
                else:
                    return t_cmp
                
            elif self_value == 3: # both had 2 pairs
                # get count dicts for both, find pair cards and cmp them
                c_dict_self = self.count_dict()
                c_dict_other = other.count_dict()

                self_pair = None
                for (c,n) in c_dict_self.items():
                    if len(n) == 2:
                        if self_pair is None:
                            self_pair = n[0]
                        else:
                            if self_pair < n[0]:
                                self_pair = n[0]

                other_pair = None
                for (c,n) in c_dict_other.items():
                    if len(n) == 2:
                        if other_pair is None:
                            other_pair = n[0]
                        else:
                            if other_pair < n[0]:
                                other_pair = n[0]

                pair_cmp = cmp(self_pair, other_pair)
                if pair_cmp == 0:
                    return cmp(self.card_list[-1], other.card_list[-1])
                else:
                    return pair_cmp

            elif self_value == 2: # both had 1 pair
                # get count dicts for both, find pair cards and cmp them
                c_dict_self = self.count_dict()
                c_dict_other = other.count_dict()

                for (c,n) in c_dict_self.items():
                    if len(n) == 2:
                        self_pair = n[0]

                for (c,n) in c_dict_other.items():
                    if len(n) == 2:
                        other_pair = n[0]

                pair_cmp = cmp(self_pair, other_pair)
                if pair_cmp == 0:
                    return cmp(self.card_list[-1], other.card_list[-1])
                else:
                    return pair_cmp
                
            else:
                return cmp(self.card_list[-1], other.card_list[-1])

        return 0

    def __str__(self):        
        return " ".join([str(c) for c in self.card_list])

player_1 = 0
player_2 = 0
tie = 0
for line in fileinput.input('problem-54.txt'):
    cards = line.strip().split(" ")
    hand1 = Hand([Card(c) for c in cards[:5]])
    hand2 = Hand([Card(c) for c in cards[5:]])
    cmp_hand = cmp(hand1, hand2)
    if cmp_hand > 0:
        player_1 += 1
    elif cmp_hand < 0:
        player_2 += 1
    else:
        tie += 1

fileinput.close()

print player_1, player_2, tie

