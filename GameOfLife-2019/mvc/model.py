import json


class GameOfLifeModel:
    def __init__(self):
        # initial states
        self.current_state = [[0 for x in range(102)] for x in range(102)]
        self.next_state = [[0 for x in range(102)] for x in range(102)]

        # initial values of dropdowns
        self.selected_rule = "Rule 1"

        # extract data from json
        with open('config_files/rule_sets.json') as rules_file:
            self.rule_sets = json.load(rules_file)        # send data from json file to rule_sets list

        with open('config_files/patterns.json') as patterns_file:
            self.pattern_sets = json.load(patterns_file)  # send data from json file to pattern_sets list
        self.pattern("Glider")

    def next(self):
        """Progress one step and then return the next state."""
        self.current_state = self.next_state
        self.next_state = self.clear_screen()  # set values to 0
        for x in range(1, 101):
            for y in range(1, 101):
                # calculate the number of alive neighbours at given coordinates
                self.neighbours_alive = self.check_neighbours_alive(x, y)

                # assign the result value from rule sets
                self.next_state[x][y] = self.rule_sets[self.selected_rule][  # selected rule name
                                        str(self.current_state[x][y])][      # 0 or 1 (dead or alive)
                                        self.neighbours_alive]               # number between 0 to 8
        return self.next_state

    # check how many neighbours of a cell are alive
    def check_neighbours_alive(self, x, y):
        # sum the value of the 8 neighbours at given coordinates
        return self.current_state[x - 1][y - 1] + self.current_state[x - 1][y] + self.current_state[x - 1][y + 1] + \
               self.current_state[x][y - 1]                     +                self.current_state[x][y + 1] + \
               self.current_state[x + 1][y - 1] + self.current_state[x + 1][y] + self.current_state[x + 1][y + 1]

    def pattern(self, name):
        self.next_state = self.clear_screen()   # set values to 0

        # verify if the name received is the same as the one from json
        if name == self.pattern_sets[0]:  # Glider
            # apply the pattern
            self.next_state[49][50] = 1
            self.next_state[50][51] = 1
            self.next_state[51][49] = 1
            self.next_state[51][50] = 1
            self.next_state[51][51] = 1
        elif name == self.pattern_sets[1]:  # Exploder
            self.next_state[48][48] = 1
            self.next_state[48][50] = 1
            self.next_state[48][52] = 1
            self.next_state[49][48] = 1
            self.next_state[49][52] = 1
            self.next_state[50][48] = 1
            self.next_state[50][52] = 1
            self.next_state[51][48] = 1
            self.next_state[51][52] = 1
            self.next_state[52][48] = 1
            self.next_state[52][50] = 1
            self.next_state[52][52] = 1
        elif name == self.pattern_sets[2]:  # Small Exploder
            self.next_state[49][49] = 1
            self.next_state[50][48] = 1
            self.next_state[50][49] = 1
            self.next_state[50][50] = 1
            self.next_state[51][48] = 1
            self.next_state[51][50] = 1
            self.next_state[52][49] = 1
        elif name == self.pattern_sets[3]:  # 10 Cell Row
            self.next_state[50][45] = 1
            self.next_state[50][46] = 1
            self.next_state[50][47] = 1
            self.next_state[50][48] = 1
            self.next_state[50][49] = 1
            self.next_state[50][50] = 1
            self.next_state[50][51] = 1
            self.next_state[50][52] = 1
            self.next_state[50][53] = 1
            self.next_state[50][54] = 1

    def clear_screen(self):
        return [[0 for x in range(102)] for x in range(102)]  # set values to 0

