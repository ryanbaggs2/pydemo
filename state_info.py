"""
Displays state information in various forms.
"""
STATES_PATH = "./data/states.json"
CAPITALS_PATH = "./data/capitals.json"
POPULATIONS_PATH = "./data/populations.json"
FLOWERS_PATH = "./data/flowers.json"


class StateInfo:

    def __init__(self, states, capitals, populations, flowers):
        """
        Instantiates the state information.

        :param states: string list containing states.
        :param capitals: string list containing state capitals.
        :param populations: string list containing state populations.
        :param flowers: string list containing state flowers.
        """
        self.states = states
        self.capitals = capitals
        self.populations = populations
        self.flowers = flowers

    def display_all_info(self):
        """
        Displays all states and their associated information to the user.
        """
        # Statement to user.
        print("\nDisplaying all states in alphabetical order:\n")

        # Loop through all states, print each one's info.
        for state_index in range(len(self.states)):
            self.display_state_info(state_index)

    def display_state_info(self, state_index):
        """
        Displays the information of a particular state.

        :param state_index: The index of the state for all lists.
        """
        print(f"State name: {self.states[state_index]}")
        print(f"Capital: {self.capitals[state_index]}")
        print(f"Population: {self.populations[state_index]}")
        print(f"Flower: {self.flowers[state_index]}\n")
