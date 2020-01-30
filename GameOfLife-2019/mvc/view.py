import tkinter as tk
from tkinter import *


class GameOfLifeView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()   # make an instance of the Tkinter class
        self.window.title("P&C's Game Of Life")
        self.window.geometry("1000x705")

        # GUI Frames
        # Frame - widget, similar to a container, used to organize the layout
        self.body_frame = Frame(self.window)
        self.body_frame.pack(side=TOP, fill=BOTH, expand=YES)
        self.left_frame = Frame(self.body_frame, background="#cccccc", borderwidth=1, width=700)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        self.right_frame = Frame(self.body_frame, background="#eeeeee", borderwidth=1, width=300)
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=YES)

        # Canvas - widget used to draw on the window
        self.canvas = tk.Canvas(self.left_frame, bg='#ffffff', highlightthickness=2, width=700)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # bind the draw_square() method to the <Button-1> event
        self.canvas.bind('<Button-1>', self.draw_square)  # event, handler

        # GUI buttons
        self.start_button = tk.Button(self.right_frame, text="Start", command=self.controller.start_action)
        self.start_button.pack(side=TOP, anchor=N, pady=5)
        self.pause_button = tk.Button(self.right_frame, text="Pause", command=self.controller.pause_action)
        self.pause_button.pack(side=TOP, anchor=N, pady=5)
        self.next_frame_button = tk.Button(self.right_frame, text="Next Frame",
                                           command=self.controller.next_frame_action)
        self.next_frame_button.pack(side=TOP, anchor=N, pady=5)
        self.randomize_button = tk.Button(self.right_frame, text="Randomize",
                                          command=self.controller.randomize_action)
        self.randomize_button.pack(side=TOP, anchor=N, pady=5)

        # dropdowns
        self.default_pattern_text = tk.StringVar(self.window)
        self.default_pattern_text.set("Default patterns")
        self.patterns_options = self.controller.patterns

        self.pattern_set_menu = tk.OptionMenu(self.right_frame, self.default_pattern_text, *self.patterns_options,
                                              command=self.controller.patterns_set_menu_action)
        self.pattern_set_menu.pack(side=TOP, anchor=N, pady=5)

        self.default_rule_text = tk.StringVar(self.window)
        self.default_rule_text.set("Change Rule")  # set default value
        # get values from controller, that takes them from the model, which takes the rule names from json file
        self.rules_options = self.controller.rules  # add the rules in the dropdown

        self.rule_set_menu = tk.OptionMenu(self.right_frame, self.default_rule_text, *self.rules_options,
                                           command=self.controller.rules_set_menu_action)
        self.rule_set_menu.pack(side=TOP, anchor=N, pady=5)

        # slider for configurable speed
        self.scale_button = tk.Scale(self.right_frame, from_=1, to=1000, length=300, orient=tk.HORIZONTAL)
        self.scale_button.set(1000)
        self.scale_button.pack(side=TOP, anchor=N, pady=5)

        # more buttons
        self.clear_button = tk.Button(self.right_frame, text="Clear",
                                      command=self.controller.clear_screen_action)
        self.clear_button.pack(side=TOP, anchor=N, pady=5)
        self.quit_button = tk.Button(self.right_frame, text="Quit", command=self.controller.quit_action)
        self.quit_button.pack(side=TOP, anchor=N, pady=5)

        self.draw_next_frame()  # draw on the canvas, the first frame, right after the application runs

    def draw_next_frame(self):
        # clear canvas
        self.canvas.delete(ALL)  # delete all objects from canvas

        # draw horizontal lines
        for y in range(0, 700, 7):
            self.canvas.create_line(0, y, 700, y, width=1, fill='#C0C0C0')

        # draw vertical lines
        for x in range(0, 700, 7):
            self.canvas.create_line(x, 0, x, 700, width=1, fill='#C0C0C0')

        # make squares A(x,y), B(x,y)
        size = 7  # size of the square (width and height)
        for i in range(1, 101):
            for j in range(1, 101):
                # check if cell is alive
                if self.controller.next_state[j][i]:  # array of arrays [j - row][i - column]
                    # draw square based on given coordinates
                    # create_rectangle(x1, y1, x2, y2, **kwargs)
                    self.canvas.create_rectangle(((i-1) * size) + 1, ((j-1) * size) + 1,
                                                 (i-1) * size + size, (j-1) * size + size,
                                                 fill='#000000', width=0)
        self.controller.user_changes = False  # mark that the user change is over

    def round_number(self, number): # round down a number (74 to 70)
        return int(number/7)*7

    def draw_square(self, event): # event - used to get position of the cursor
        self.controller.user_changes = True  # mark that the user change is started
        size = 7  # size of the square (width and height)
        for i in range(1, 101):
            for j in range(1, 101):
                # check if the cursor x and y coordinates correspond to the matrix coordinates
                if i == self.round_number(event.x)/size and j == self.round_number(event.y)/size:
                    if self.controller.next_state[j+1][i+1] == 1: # if cell is alive, then it becomes dead
                        self.controller.next_state[j+1][i+1] = 0
                    else: # if cell is dead, then it becomes alive
                        self.controller.next_state[j+1][i+1] = 1
        # draw next frame, without processing (verifying the neighbours) of the next state
        self.controller.next_frame_action()
