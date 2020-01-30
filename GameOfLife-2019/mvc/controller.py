import mvc.model
import mvc.view
import random


class GameOfLifeController:
    def __init__(self):  # initializer (it's the first piece of code executed in a newly created instance of the class)
        """ initialize variables """
        self.model = mvc.model.GameOfLifeModel()  # make an instance of the model class

        # declare before initializing the view, because draw_next_frame() needs self.controller.next_state
        self.next_state = self.model.next_state
        self.user_changes = False  # boolean used to notify when the user clicks on canvas or changes pattern

        self.rules = []   # rule names from json file
        self.patterns = []  # pattern names from json file
        self.get_rule_names()
        self.get_pattern_names()
        self.view = mvc.view.GameOfLifeView(self)  # make an instance of the view class

        self.view.window.mainloop()  # opens the application window

    def start_action(self):  # call when the start button is pressed
        self.next_state = self.model.next()
        self.view.draw_next_frame()
        # after(delay, callback)
        # call start_action function after a delay in milliseconds
        self.task = self.view.window.after(1001-self.view.scale_button.get(), self.start_action)
        # disable and enable buttons
        self.view.pause_button["state"] = "normal"
        self.view.start_button["state"] = "disabled"

    def pause_action(self):  # call when the pause button is pressed
        # stop calling the start_action from the task
        self.view.window.after_cancel(self.task)
        # disable and enable buttons
        self.view.pause_button["state"] = "disabled"
        self.view.start_button["state"] = "normal"

    def next_frame_action(self):  # call when the next frame button is pressed
        self.model.next_state = self.next_state
        # process the next frame only if the user didn't made changes on the frame (if false)
        if not self.user_changes:
            self.next_state = self.model.next()      # process next frame
        self.view.draw_next_frame()                  # draw next frame

    def randomize_action(self):  # call when the randomize button is pressed
        for i in range(1, 101):
            for j in range(1, 101):
                if random.uniform(0, 1) > 0.5:
                    self.model.next_state[i][j] = 1
                else:
                    self.model.next_state[i][j] = 0
        self.user_changes = True  # notify that the user changed pattern
        self.next_frame_action()

    def rules_set_menu_action(self, selection):  # call when the rules dropdown is opened
        self.model.selected_rule = selection  # assign value from dropdown

    def patterns_set_menu_action(self, selection):  # call when the patterns dropdown is opened
        self.model.pattern(selection)  # set the pattern based on name
        self.next_state = self.model.next_state  # get values from model
        self.user_changes = True  # notify that the user changed pattern
        self.next_frame_action()

    def clear_screen_action(self):  # call when the clear screen button is pressed
        self.next_state = self.model.clear_screen()  # sets the next_state elements to 0
        self.next_frame_action()

    def quit_action(self):  # call when the quit button is pressed
        self.view.window.destroy()

    def get_rule_names(self):
        for k, v in self.model.rule_sets.items():  # go for each set of keys and values
            self.rules.append(k)  # add the keys (rule names) on the list

    def get_pattern_names(self):
        for i in self.model.pattern_sets:  # go through the list of patterns
            self.patterns.append(i)  # add the keys (pattern names) on the list
