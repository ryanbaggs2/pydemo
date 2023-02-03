"""
Name: Baggs, Ryan     SDEV 300-6980    Date: 07/08/2022

Program displays various state information through a menu of options for
displaying or searching.
"""
# For exiting.
import sys

# MatPlotLib for the graph and images.
import matplotlib.pyplot as plot
import matplotlib.image as img

# Selection options.
DISPLAY_INFO = 1
SEARCH = 2
TOP_5 = 3
UPDATE = 4
EXIT = 0

# Menu minimum and maximum.
MENU_MIN = 0
MENU_MAX = 4

# State population min and max values, 1k and 100 mil.
POP_MIN = 1000
POP_MAX = 100000000

# States.
STATES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
          "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
          "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
          "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
          "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
          "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
          "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
          "Washington", "West Virginia", "Wisconsin", "Wyoming"]

CAPITALS = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford",
            "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis",
            "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston",
            "Lansing", "St. Paul", "Jackson", "Jefferson City", "Helena", "Lincoln",
            "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismark",
            "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia",
            "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond",
            "Olympia", "Charleston", "Madison", "Cheyenne"]

FLOWERS = ["Camellia", "Forget Me Not", "Saguaro Cactus Blossom", "Apple Blossom",
           "California Poppy", "White and Lavender Columbine", "Mountain Laurel", "Peach Blossom",
           "Orange Blossom", "Cherokee Rose", "Hibiscus", "Syringa", "Purple Violet", "Peony",
           "Wild Prairie Rose", "Sunflower", "Goldenrod", "Magnolia",
           "White Pine Cone and Tassel", "Black-Eyed Susan", "Mayflower", "Apple Blossom",
           "Pink and White Lady Slipper", "Magnolia", "White Hawthorn Blossom", "Bitterroot",
           "Goldenrod", "Sagebrush", "Purple Lilac", "Violet", "Yucca Flower", "Rose", "Dogwood",
           "Scarlet Carnation", "Mistletoe", "Oregon Grape", "Mountain Laurel", "Violet",
           "Yellow Jessamine", "Wild Prairie Rose", "Pasque Flower", "Iris", "Bluebonnet",
           "Sego Lily", "Red Clover", "Dogwood", "Pink Rhododendron", "Rhododendron",
           "Wood Violet", "Indian Paintbrush"]

POPULATIONS = [4918689, 727951, 7399410, 3025875, 39562858, 5826185, 3559054, 982049, 21711157,
               10723715, 1411151, 1823594, 12620571, 6768941, 3161522, 2915269, 4474193, 4637898,
               1349367, 6055558, 6902371, 9989642, 5673015, 2971278, 6153233, 1076891, 1943202,
               3132971, 1365957, 8878355, 2100917, 19376771, 10594553, 766044, 11701859, 3973707,
               4253588, 12803056, 1060435, 5213272, 890620, 6886717, 29363096, 3258366, 623620,
               8569752, 7705917, 1780003, 5837462, 579917]


def main():
    """ Main function."""
    print("Welcome to the state information program.\n")

    menu()
    exit_program()


def menu():
    """
    Prints out a menu of options for the user, and executes their
    selection.
    """
    running = True

    while running:
        print("Please enter what you would like to do:")
        print("Enter 1 to display all state information.")
        print("Enter 2 to search for a specific state and display its information.")
        print("Enter 3 to display the top 5 states with largest populations.")
        print("Enter 4 update a state's population.")
        print("Enter 0 to exit.")

        exec_menu_selection(get_num_input(MENU_MIN, MENU_MAX))


def exec_menu_selection(selection):
    """
    Executes the menu selection (function) to perform the specified
    operation.

    :param selection: of the user.
    """
    # Check what the user selected and execute it's corresponding function.
    # Display state information alphabetically.
    if selection == DISPLAY_INFO:
        display_all_info()

    # Search for a specific state and its info.
    if selection == SEARCH:
        search_for_state()

    #
    if selection == TOP_5:
        display_top_five()

    #
    if selection == UPDATE:
        update_state_pop()

    # Exit the program safely.
    if selection == EXIT:
        exit_program()


def get_num_input(minimum, maximum):
    """
    Gets the input from the user within the specified minimum, and maximum.

    :param minimum: the minimum accepted for the value.
    :param maximum: the maximum accepted for the value.
    :return: the user input within the specified bounds.
    """
    while True:
        # Catch any invalid values and raise an error and re-ask
        # for input.
        try:
            # Get the user input.
            user_input = int(input("\nPlease enter your value: "))

            # Check if the user input is valid.
            if user_input < minimum or user_input > maximum:
                # Value is below minimum or above maximum. Raise a ValueError.
                raise ValueError()

            # User input is valid.
            return user_input

        except ValueError:
            # Raise an Exception. ValueError as the input is not valid.
            print("Please enter a valid value, must be an integer within "
                  "the bounds.\n")

            # Continue the while loop.
            continue


def display_all_info():
    """
    Displays all states and their associated information to the user.
    """
    # Statement to user.
    print("\nDisplaying all states in alphabetical order:\n")

    # Loop through all states, print each one's info.
    for state_index in range(len(STATES)):
        display_state_info(state_index)


def display_state_info(state_index):
    """
    Displays the information of a particular state.

    :param state_index: The index of the state for all lists.
    """
    print(f"State name: {STATES[state_index]}")
    print(f"Capital: {CAPITALS[state_index]}")
    print(f"Population: {POPULATIONS[state_index]}")
    print(f"Flower: {FLOWERS[state_index]}\n")


def search_for_state():
    """
    Searches for the user specified state and prints its information.
    """
    # Statement to user.
    print("\nSearch for a state: \n")

    # Get the state input.
    state_input = get_state_input()

    # Get the index of the state.
    state_index = STATES.index(state_input)

    # Print the state info by passing the index to the associated display
    # function.
    display_state_info(state_index)

    # Display the state flower image.
    display_state_flower(state_index)


def get_state_input():
    """
    Gets the state input from the user and returns the string value.

    :return: the valid state.
    """
    # Valid state flag.
    valid_state = False

    # Initialize user input.
    user_input = None

    # Loop until valid state
    while not valid_state:
        # Get user input.
        user_input = input("\nPlease enter the full state name, "
                           "not case sensitive, EX: California: ")

        # Modify capitalization of state to match list values.
        user_input = user_input.lower().capitalize()

        # Update flag if the state is in the STATES list.
        valid_state = user_input in STATES

        # Check if input was invalid.
        if valid_state is False:
            # Input was not valid, inform user.
            print("Please enter a valid state.")

    # Valid state found, return the state.
    return user_input


def display_state_flower(state_index):
    """
    Displays a specified state's state flower.

    :param state_index: The index of the state to display its state flower.
    """
    # Print statement for user.
    print("\nDisplay state flower:\n")
    # Create the file path.
    path = "../week3/flowers/" + FLOWERS[state_index].lower() + ".jpg"

    # Read the image from the file path.
    image = img.imread(path)

    # Create a plot of the image.
    plot.imshow(image)

    # Add titles for the state and flower.
    plot.suptitle(STATES[state_index])
    plot.title(FLOWERS[state_index])

    # Show the plot.
    plot.show()


def display_top_five():
    """
    Displays the top five states by population as a bar graph to the user.
    """
    # Statement to user.
    print("\nDisplay top five states with largest populations:\n")

    # Create temporary list of populations.
    descending_pop = POPULATIONS.copy()

    # Sort the list into descending order.
    descending_pop.sort()
    descending_pop.reverse()

    # Create a list of indexes of the states.
    indexes = []

    # Current index tracker.
    i = 0

    # Iterate through first 5 indexes of list.
    for population in descending_pop[0:4]:
        # Add the index of the population to the indexes list.
        indexes.append(POPULATIONS.index(population))

        # Increment index.
        i += 1

    # Reset index tracker.
    i = 0

    # Create list of top states.
    top_states = []

    # Iterate through the list of indexes.
    for index in indexes:
        # Get the state associated with that index and add it to the
        # top_states list.
        top_states.append(STATES[index])

        # Increment index.
        i += 1

    # Make a bar graph of top_states and their populations.
    plot.bar(top_states, descending_pop[0:4])

    # Labels.
    plot.ylabel("Populations")
    plot.xlabel("States")
    plot.suptitle("Top 5 States by Population")

    # Scale.
    plot.yscale('linear')

    # Display the bar graph.
    plot.show()


def update_state_pop():
    """
    Updates a state's population to a user entered value.
    """
    # Print statement to user.
    print("\nUpdate state population:")

    # Get the state to modify.
    state = get_state_input()

    # Print statement to user.
    print("Please enter the updated state population:")

    # Get the updated population.
    updated_pop = get_num_input(POP_MIN, POP_MAX)

    # Update the state population.
    POPULATIONS[STATES.index(state)] = updated_pop

    # Print statement to user informing completion.
    print(f"{state} has been updated to a population of: {updated_pop}")


def exit_program():
    """ Prints an exit statement and exits program."""
    print("Thank you for using the state information program! Now exiting...")
    sys.exit()


main()
