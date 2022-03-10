# Author: Carleton Foster
# GitHub username: carletoniii
# Date: 9 March 2022
# Description: Portfolio Project: Program with a class called ShipGame that allows two people to play the game
# Battleship. Each player has their own 10x10 grid they place their ships on. On their turn, they can fire a torpedo at
# a square on the enemy's grid. Player 'first' gets the first turn to fire a torpedo, after which players alternate
# firing torpedoes. A ship is sunk when all of its squares have been hit. When a player sinks their opponent's final
# ship, they win.

class ShipGame:
    """
    Class that that allows two people to play the game Battleship. Each player has their own 10x10 grid they place
    their ships on. On their turn, they can fire a torpedo at a square on the enemy's grid. Player 'first' gets the
    first turn to fire a torpedo, after which players alternate firing torpedoes. A ship is sunk when all of its squares
    have been hit. When a player sinks their opponent's final ship, they win.
    """

    def __init__(self):
        """This method sets all data members to their initial values."""
        self._player1_board = {'651': ' ', '652': ' ', '653': ' ', '654': ' ', '655': ' ',
                               '656': ' ', '657': ' ', '658': ' ', '659': ' ', '6510': ' ',
                               '661': ' ', '662': ' ', '663': ' ', '664': ' ', '665': ' ',
                               '666': ' ', '667': ' ', '668': ' ', '669': ' ', '6610': ' ',
                               '671': ' ', '672': ' ', '673': ' ', '674': ' ', '675': ' ',
                               '676': ' ', '677': ' ', '678': ' ', '679': ' ', '6710': ' ',
                               '681': ' ', '682': ' ', '683': ' ', '684': ' ', '685': ' ',
                               '686': ' ', '687': ' ', '688': ' ', '689': ' ', '6810': ' ',
                               '691': ' ', '692': ' ', '693': ' ', '694': ' ', '695': ' ',
                               '696': ' ', '697': ' ', '698': ' ', '699': ' ', '6910': ' ',
                               '701': ' ', '702': ' ', '703': ' ', '704': ' ', '705': ' ',
                               '706': ' ', '707': ' ', '708': ' ', '709': ' ', '7010': ' ',
                               '711': ' ', '712': ' ', '713': ' ', '714': ' ', '715': ' ',
                               '716': ' ', '717': ' ', '718': ' ', '719': ' ', '7110': ' ',
                               '721': ' ', '722': ' ', '723': ' ', '724': ' ', '725': ' ',
                               '726': ' ', '727': ' ', '728': ' ', '729': ' ', '7210': ' ',
                               '731': ' ', '732': ' ', '733': ' ', '734': ' ', '735': ' ',
                               '736': ' ', '737': ' ', '738': ' ', '739': ' ', '7310': ' ',
                               '741': ' ', '742': ' ', '743': ' ', '744': ' ', '745': ' ',
                               '746': ' ', '747': ' ', '748': ' ', '749': ' ', '7410': ' '}
        self._player2_board = {'651': ' ', '652': ' ', '653': ' ', '654': ' ', '655': ' ',
                               '656': ' ', '657': ' ', '658': ' ', '659': ' ', '6510': ' ',
                               '661': ' ', '662': ' ', '663': ' ', '664': ' ', '665': ' ',
                               '666': ' ', '667': ' ', '668': ' ', '669': ' ', '6610': ' ',
                               '671': ' ', '672': ' ', '673': ' ', '674': ' ', '675': ' ',
                               '676': ' ', '677': ' ', '678': ' ', '679': ' ', '6710': ' ',
                               '681': ' ', '682': ' ', '683': ' ', '684': ' ', '685': ' ',
                               '686': ' ', '687': ' ', '688': ' ', '689': ' ', '6810': ' ',
                               '691': ' ', '692': ' ', '693': ' ', '694': ' ', '695': ' ',
                               '696': ' ', '697': ' ', '698': ' ', '699': ' ', '6910': ' ',
                               '701': ' ', '702': ' ', '703': ' ', '704': ' ', '705': ' ',
                               '706': ' ', '707': ' ', '708': ' ', '709': ' ', '7010': ' ',
                               '711': ' ', '712': ' ', '713': ' ', '714': ' ', '715': ' ',
                               '716': ' ', '717': ' ', '718': ' ', '719': ' ', '7110': ' ',
                               '721': ' ', '722': ' ', '723': ' ', '724': ' ', '725': ' ',
                               '726': ' ', '727': ' ', '728': ' ', '729': ' ', '7210': ' ',
                               '731': ' ', '732': ' ', '733': ' ', '734': ' ', '735': ' ',
                               '736': ' ', '737': ' ', '738': ' ', '739': ' ', '7310': ' ',
                               '741': ' ', '742': ' ', '743': ' ', '744': ' ', '745': ' ',
                               '746': ' ', '747': ' ', '748': ' ', '749': ' ', '7410': ' '}
        self._player1_ship_dict = dict()
        self._player2_ship_dict = dict()
        self._turn_history = dict()

    def print_board(self, player):
        """Prints the current board of the specified player."""
        if player == 'first':
            counter = 0
            print(' 1 2 3 4 5 6 7 8 9 10')
            row_counter = 65
            print(chr(row_counter), end='')
            row_counter += 1
            for x in self._player1_board.values():
                print(x, end=' ')
                counter += 1
                if counter == 10:
                    print('\n', end='')
                    if row_counter == 75:
                        print('\n', end='')
                        break
                    print(chr(row_counter), end='')
                    row_counter += 1
                    counter = 0
        if player == 'second':
            counter = 0
            print(' 1 2 3 4 5 6 7 8 9 1 0')
            row_counter = 65
            print(chr(row_counter), end='')
            row_counter += 1
            for x in self._player2_board.values():
                print(x, end=' ')
                counter += 1
                if counter == 10:
                    print('\n', end='')
                    if row_counter == 75:
                        print('\n', end='')
                        break
                    print(chr(row_counter), end='')
                    row_counter += 1
                    counter = 0

    def place_ship(self, player, ship_length, occupying_coord, orientation):
        """
        place_ship takes as arguments: the player (either 'first' or 'second'), the length of the ship, the coordinates
        of the square it will occupy that is closest to A1, and the ship's orientation - either 'R' if its squares
        occupy the same row, or 'C' if its squares occupy the same column. If a ship would not fit entirely on that
        player's grid, or if it would overlap any previously placed ships on that player's grid, or if the length of
        the ship is less than 2, the ship should not be added and the method should return False. Otherwise, the ship
        should be added and the method should return True. You may assume that all calls to place_ship() are made
        before any other methods are called (besides the init method, of course). You should not enforce turn order
        during the placement phase.
        """
        occupying_coord = str(ord(occupying_coord[:1])) + occupying_coord[1:]
        if ship_length < 2:
            return False
        elif ship_length > 10:
            return False
        elif orientation == 'R' and len(occupying_coord) == 4:
            return False
        elif orientation == 'R' and ((int(occupying_coord[-1:]) - 1) + ship_length) > 10:
            return False
        elif orientation == 'C' and occupying_coord[:2] == '74':
            return False
        elif orientation == 'C' and ((int(occupying_coord[:2])) - 1) + ship_length > 74:
            return False
        else:
            if player == 'first':
                if orientation == 'R':
                    temp_coord = occupying_coord
                    for x in range(ship_length):
                        if self._player1_board[temp_coord] == 'x':
                            return False
                        temp_coord = temp_coord[:2] + (str(int(temp_coord[2:]) + 1))
                    ship_list = list()
                    for x in range(ship_length):
                        self._player1_board[occupying_coord] = 'x'
                        ship_list.append(occupying_coord)
                        occupying_coord = occupying_coord[:2] + (str(int(occupying_coord[2:]) + 1))
                    self._player1_ship_dict[str(len(self._player1_ship_dict) + 1)] = ship_list
                    return True
                elif orientation == 'C':
                    temp_coord = occupying_coord
                    for x in range(ship_length):
                        if self._player1_board[temp_coord] == 'x':
                            return False
                        temp_coord = (str(int(temp_coord[:2]) + 1)) + occupying_coord[2:]
                    ship_list = list()
                    for x in range(ship_length):
                        self._player1_board[occupying_coord] = 'x'
                        ship_list.append(occupying_coord)
                        occupying_coord = (str(int(occupying_coord[:2]) + 1)) + occupying_coord[2:]
                    self._player1_ship_dict[str(len(self._player1_ship_dict) + 1)] = ship_list
                    return True
            elif player == 'second':
                if orientation == 'R':
                    temp_coord = occupying_coord
                    for x in range(ship_length):
                        if self._player2_board[temp_coord] == 'x':
                            return False
                        temp_coord = temp_coord[:2] + (str(int(temp_coord[2:]) + 1))
                    ship_list = list()
                    for x in range(ship_length):
                        self._player2_board[occupying_coord] = 'x'
                        ship_list.append(occupying_coord)
                        occupying_coord = occupying_coord[:2] + (str(int(occupying_coord[2:]) + 1))
                    self._player2_ship_dict[str(len(self._player2_ship_dict) + 1)] = ship_list
                    return True
                elif orientation == 'C':
                    temp_coord = occupying_coord
                    for x in range(ship_length):
                        if self._player2_board[temp_coord] == 'x':
                            return False
                        temp_coord = (str(int(temp_coord[:2]) + 1)) + occupying_coord[2:]
                    ship_list = list()
                    for x in range(ship_length):
                        self._player2_board[occupying_coord] = 'x'
                        ship_list.append(occupying_coord)
                        occupying_coord = (str(int(occupying_coord[:2]) + 1)) + occupying_coord[2:]
                    self._player2_ship_dict[str(len(self._player2_ship_dict) + 1)] = ship_list
                    return True

    def _ship_status(self, player, ship_num):
        """
        This private method will return the status of a specific ship. If none of a ship's occupying coordinates are
        equal to 'x', this function will return 'sunk'. Otherwise, this function will return 'afloat'.
        """
        if player == 'first':
            for x in self._player1_ship_dict[ship_num]:
                if self._player1_board[x] == 'x':
                    return 'afloat'
            return 'sunk'
        elif player == 'second':
            for x in self._player2_ship_dict[ship_num]:
                if self._player2_board[x] == 'x':
                    return 'afloat'
            return 'sunk'

    def get_current_state(self):
        """
        get_current_state returns the current state of the game: either 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'.
        """
        if self.get_num_ships_remaining('first') > 0 and self.get_num_ships_remaining('second') == 0:
            return 'FIRST_WON'
        elif self.get_num_ships_remaining('second') > 0 and self.get_num_ships_remaining('first') == 0:
            return 'SECOND_WON'
        else:
            return 'UNFINISHED'

    def fire_torpedo(self, player, target_coord):
        """
        fire_torpedo takes as arguments the player firing the torpedo (either 'first' or 'second') and the coordinates
        of the target square, e.g. 'B7'. If it's not that player's turn, or if the game has already been won, it should
        just return False. Otherwise, it should record the move, update whose turn it is, update the current state (if
        this turn sank the opponent's final ship), and return True. If that player has fired on that square before,
        that's not illegal - it just wastes a turn. You can assume place_ship will not be called after firing of the
        torpedoes has started.
        """
        target_coord = str(ord(target_coord[:1])) + target_coord[1:]
        if len(self._turn_history) == 0:
            self._turn_history['1'] = player
            if player == 'first':
                if self._player2_board[target_coord] == 'x':
                    self._player2_board[target_coord] = 'o'
                return True
            elif player == 'second':
                if self._player1_board[target_coord] == 'x':
                    self._player1_board[target_coord] = 'o'
                return True
        elif self.get_current_state() != 'UNFINISHED':
            return False
        elif self._turn_history[str(len(self._turn_history))] == player:
            return False
        else:
            self._turn_history[str(len(self._turn_history) + 1)] = player
            if player == 'first':
                if self._player2_board[target_coord] == 'x':
                    self._player2_board[target_coord] = 'o'
                return True
            elif player == 'second':
                if self._player1_board[target_coord] == 'x':
                    self._player1_board[target_coord] = 'o'
                return True

    def get_num_ships_remaining(self, player):
        """
        get_num_ships_remaining takes as an argument either "first" or "second" and returns how many ships the specified
        player has left.
        """
        ship_count = 0
        if player == 'first':
            for x in self._player1_ship_dict:
                if self._ship_status(player, x) == 'afloat':
                    ship_count += 1
        elif player == 'second':
            for x in self._player2_ship_dict:
                if self._ship_status(player, x) == 'afloat':
                    ship_count += 1
        return ship_count
