# Implements monopoly simulation
#
# only set up for one player
#
# http://projecteuler.net/index.php?section=problems&id=84
import random
import re


# returns tuple of dice roll
def roll_dice(num_sides):
    r1 = random.randint(1, num_sides)
    r2 = random.randint(1, num_sides)
    return (r1,r2)
    
def is_double(dice_result):
    return dice_result[0] == dice_result[1]

class Board:
    num_spaces = 40    
    name_to_index = {
            'GO': 0, 'A1': 1, 'CC1': 2, 'A2': 3, 'T1': 4, 'R1': 5,
            'B1': 6, 'CH1': 7, 'B2': 8, 'B3': 9, 'JAIL': 10, 'C1': 11,
            'U1': 12, 'C2': 13, 'C3': 14, 'R2': 15, 'D1': 16, 'CC2':
            17, 'D2': 18, 'D3': 19, 'FP': 20, 'E1': 21, 'CH2': 22,
            'E2': 23, 'E3': 24, 'R3': 25, 'F1': 26, 'F2': 27, 'U2':
            28, 'F3': 29, 'G2J': 30, 'G1': 31, 'G2': 32, 'CC3': 33,
            'G3': 34, 'R4': 35, 'CH3': 36, 'H1': 37, 'T2': 38, 'H2':
            39}

    index_to_name = {}
    for (k,v) in name_to_index.items():
        index_to_name[v] = k  

    num_utilities = 2
    num_rr = 4
    num_cc = 3
    num_ch = 3
    
    utility_rex = re.compile('^U(\d)$')
    rr_rex = re.compile('^R(\d)$')
    cc_rex = re.compile('^CC(\d)$')
    ch_rex = re.compile('^CH(\d)$')

    # return next amount space on board
    def advance_spaces(current_space, amount):
        return (current_space + amount) % Board.num_spaces
    advance_spaces = staticmethod(advance_spaces)

    # return next space on board
    def next_space(current_space):
        return Board.advance_spaces(current_space, 1)
    next_space = staticmethod(next_space)

    def special_space(pattern, space_index):
        if Board.index_to_name.has_key(space_index):
            m = re.match(pattern, Board.index_to_name[space_index])
            if m:
                return m.groups()[0]
        return None
    special_space = staticmethod(special_space)

    def next_special_space(pattern, space_index):
        current_space = space_index
        while not Board.special_space(pattern, current_space):
            current_space = Board.next_space(current_space)
        return current_space
    next_special_space = staticmethod(next_special_space)
       
    def utility(space_index):
        return Board.special_space(Board.utility_rex, space_index)
    utility = staticmethod(utility)

    def next_utility(space_index):
        return Board.next_special_space(Board.utility_rex, space_index)
    next_utility = staticmethod(next_utility)

    def railway(space_index):
        return Board.special_space(Board.rr_rex, space_index)
    railway = staticmethod(railway)

    def next_railway(space_index):
        return Board.next_special_space(Board.rr_rex, space_index)
    next_railway = staticmethod(next_railway)

    def community_chest(space_index):
        return Board.special_space(Board.cc_rex, space_index)
    community_chest = staticmethod(community_chest)

    def chance(space_index):
        return Board.special_space(Board.ch_rex, space_index)
    chance = staticmethod(chance)


# define some board constants
##GO = 0
##R = (5, 15, 25, 35)
##U = (12, 28)
##JAIL = 10
##C1 = 11
##E3 = 24
##G2JAIL = 30
##H2 = 39
##COMMUNITY_CHEST = (2, 17,33)
##CHANCE = (7,22,36)
##
##NUM_SIDES = 6


##Community Chest (2/16 cards):
##Advance to GO
##Go to JAIL
##Chance (10/16 cards):
##Advance to GO (0)
##Go to JAIL (1)
##Go to C1 (2)
##Go to E3 (3)
##Go to H2 (4)
##Go to R1 (5)
##Go to next R (railway company) (6)
##Go to next R (7)
##Go to next U (utility company) (8)
##Go back 3 squares. (9)
class CardDeck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.cards = range(0, 16)
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards[0]
        self.cards.pop(0)
        self.cards.append(card)
        return card

    def is_advance_to_go(self, card):
        return card == 0

    def is_goto_jail(self, card):
        return card == 1

    def is_goto_c1(self, card):
        return card == 2

    def is_goto_e3(self, card):
        return card == 3

    def is_goto_h2(self, card):
        return card == 4

    def is_goto_r1(self, card):
        return card == 5

    def is_goto_next_r(self, card):
        return (card == 6 or card == 7)

    def is_goto_next_u(self, card):
        return card == 8

    def is_go_back(self, card):
        return card == 9

class Player:
    def __init__(self):
        self.current_space = 0
        self.num_doubles = 0

    def advance_spaces(self, add_spaces):
        self.current_space = Board.advance_spaces(self.current_space, add_spaces)

    def set_space(self, new_space):
        self.current_space = new_space % Board.num_spaces

    def advance_to_go(self):
        self.current_space = Board.name_to_index['GO']

    def goto_jail(self):
        self.current_space = Board.name_to_index['JAIL']

    def goto_next_utility(self):
        self.current_space = Board.next_utility(self.current_space)

    def goto_next_railway(self):
        self.current_space = Board.next_railway(self.current_space)
    

class Game:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.player = Player()
        self.chance_deck = CardDeck()
        self.cc_deck = CardDeck()

    # rolls dice and returns the final board position
    # of player
    # if 3 doubles have been rolled in a row, sends piece to jail
    # if lands on go to jail, sends piece to jail
    # if lands on community chest or chance square,
    # draws card and follows instructions
    def play_turn(self):
        dice_result = roll_dice(self.num_sides)

        # check the double count
        if is_double(dice_result):
            self.player.num_doubles += 1
        else:
            self.player.num_doubles = 0

        if self.player.num_doubles == 3:
            self.player.num_doubles = 0
            self.player.goto_jail()
            return
            
        num_spaces = sum(dice_result)
        self.player.advance_spaces(num_spaces)
    
        # check if go to jail
        if self.player.current_space == Board.name_to_index['G2J']:
            self.player.goto_jail()
            return
    
        # check if on community chest
        if Board.community_chest(self.player.current_space):
            card = self.cc_deck.draw()
            if self.cc_deck.is_goto_jail(card):
                self.player.goto_jail()

            if self.cc_deck.is_advance_to_go(card):
                self.player.advance_to_go()

            return

        # if on chance
        if Board.chance(self.player.current_space):
            card = self.chance_deck.draw()
            if self.chance_deck.is_goto_jail(card):
                self.player.goto_jail()

            if self.chance_deck.is_advance_to_go(card):
                self.player.advance_to_go()

            if self.chance_deck.is_goto_c1(card):
                self.player.set_space(Board.name_to_index['C1'])

            if self.chance_deck.is_goto_e3(card):
                self.player.set_space(Board.name_to_index['E3'])

            if self.chance_deck.is_goto_h2(card):
                self.player.set_space(Board.name_to_index['H2'])

            if self.chance_deck.is_goto_r1(card):
                self.player.set_space(Board.name_to_index['R1'])

            if self.chance_deck.is_goto_next_r(card):
                self.player.goto_next_railway()

            if self.chance_deck.is_goto_next_u(card):
                self.player.goto_next_utility()

            if self.chance_deck.is_go_back(card):
                self.player.advance_spaces(-3)

            return      
    
def run_simulation(num_rolls):
    board_positions = {}
    g = Game(4)
    for i in xrange(0, num_rolls):
        g.play_turn()
        if not board_positions.has_key(g.player.current_space):
            board_positions[g.player.current_space] = 0
        board_positions[g.player.current_space] += 1

    return board_positions


if __name__ == '__main__':
    num_rolls = 1000000
    board_positions = run_simulation(num_rolls)

    sorted_positions = sorted(board_positions.iteritems(), key=lambda (k,v): (v,k), reverse=True)

    for (k,v) in sorted_positions:
        print k, '=', 100.0 * float(v) / float(num_rolls)
    
