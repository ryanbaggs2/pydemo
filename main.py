"""
Performs the menu operations for the program.
"""
# For exit function.
import sys
import file_rw
from state_info import StateInfo, STATES_PATH, CAPITALS_PATH, \
    POPULATIONS_PATH, FLOWERS_PATH

# All menu's option.
EXIT = 0
GO_BACK = 5

# Main menu options.
MATRIX_OPS = 1
PASS_OPS = 2
STATE_INFO = 3

# Matrix ops menu options.
ADD = 1
SUB = 2
MUL = 3
ELEM_BY_ELEM_MUL = 4

# Password ops menu options.
LOG_IN = 1
CREATE_ACC = 2
PASS_GO_BACK = 3

# State info menu options.
DISPLAY_INFO = 1
SEARCH = 2
TOP_5 = 3
UPDATE = 4


def main():
    """
    Main function.

    Prints a welcome statement and starts the menu selection process for the
    program.
    """
    print("Welcome to PyDemo, a program demonstrating some of the programming "
          "skills I have learned")

    main_menu()


def main_menu():
    """
    Print the main menu, loop and get the users menu selection.
    """
    while True:
        # Print welcome statement to user.
        print("\nPlease enter what you would like to do: ")

        # Print the menu to the user.
        print("Enter 1 to perform matrix operations.")
        print("Enter 2 to perform password operations.")
        print("Enter 3 for US state information.")
        print("Enter 0 to exit.")

        # Get the users menu selection and execute its corresponding function.
        exec_main_menu(get_num_input(EXIT, STATE_INFO))


def exec_main_menu(selection):
    """
    Executes the corresponding main menu function.

    :param selection: of the user.
    """
    if selection is MATRIX_OPS:
        matrix_ops()

    if selection is PASS_OPS:
        pass_ops()

    if selection is STATE_INFO:
        state_info()

    if selection is EXIT:
        exit_program()


def get_num_input(minimum, maximum):
    """
    Gets input from the user within the specified minimum, and maximum.

    :param minimum: the minimum accepted for the value.
    :param maximum: the maximum accepted for the value.
    :return: the user input value.
    """
    while True:
        # Catch any invalid values and raise an error and re-ask
        # for input.
        try:
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

            # Loop until valid input returned.
            continue


def matrix_ops():
    """
    Sets up a menu of options to perform matrix calculations to add,
    subtract, matrix multiplication, and element-wise multiplication.
    """
    while True:
        # Print menu for the matrix operation.
        print("\nMatrix operations menu:")
        print("Enter 1 to add two matrices.")
        print("Enter 2 to subtract two matrices.")
        print("Enter 3 to multiply two matrices.")
        print("Enter 4 to element by element multiplication for two matrices.")
        print("Enter 5 to return to the main menu.")
        print("Enter 0 to exit.")

        # Get the users menu selection and execute its corresponding function.
        exec_matrix_ops_sel(get_num_input(EXIT, GO_BACK))


def exec_matrix_ops_sel(selection):
    """
    Executes the corresponding matrix operations menu function.

    :param selection: of the user.
    """
    if selection is ADD:
        pass

    if selection is SUB:
        pass

    if selection is MUL:
        pass

    if selection is ELEM_BY_ELEM_MUL:
        pass

    if selection is GO_BACK:
        main_menu()

    exec_sub_menus_sel(selection)


def pass_ops():
    """
    Requests user to log in, validating the credentials. After log in allows
    encoding of a message.
    """
    while True:
        # Print menu.
        print("\nPassword operations menu:")
        print("Enter 1 to log in.")
        print("Enter 2 to create an account.")
        print("Enter 3 to return to the main menu.")
        print("Enter 0 to exit.")

        # Get the users menu selection and execute its corresponding function.
        exec_pass_ops_sel(get_num_input(EXIT, PASS_GO_BACK))


def exec_pass_ops_sel(selection):
    """
    Executes the corresponding password operations menu function.

    :param selection: of the user.
    """
    if selection is LOG_IN:
        pass

    if selection is CREATE_ACC:
        pass

    if selection is PASS_GO_BACK:
        main_menu()

    exec_sub_menus_sel(selection)


def state_info():
    """
    Displays menu of options to: display the state, its capital, population,
    and flower, or modify the state population; search for a specific state's
    info; display the top 5 states by population; or update a specific state's
    population.
    """
    while True:
        # Print menu.
        print("\nState info menu:")
        print("Enter 1 to display all state information.")
        print("Enter 2 to search for a specific state and display its information.")
        print("Enter 3 to display the top 5 states with largest populations.")
        print("Enter 4 update a state's population.")
        print("Enter 5 to return to the main menu.")
        print("Enter 0 to exit.")

        # Get the users menu selection and execute its corresponding function.
        exec_state_info_sel(get_num_input(EXIT, GO_BACK))


def exec_state_info_sel(selection):
    """
    Executes the corresponding state info menu function.

    :param selection: of the user.
    """
    # Read in and initialize state information.
    info = StateInfo(file_rw.read(STATES_PATH),
                     file_rw.read(CAPITALS_PATH),
                     file_rw.read(POPULATIONS_PATH),
                     file_rw.read(FLOWERS_PATH))

    if selection is DISPLAY_INFO:
        info.display_all_info()

    if selection is SEARCH:
        pass

    if selection is TOP_5:
        pass

    if selection is UPDATE:
        pass

    if selection is GO_BACK:
        main_menu()

    exec_sub_menus_sel(selection)


def exec_sub_menus_sel(selection):
    """
    Executes the corresponding function selected. These options are found on
    all sub menus.

    :param selection: of the user.
    """

    if selection is EXIT:
        exit_program()


def exit_program():
    """ Prints an exit statement and exits program."""
    print("Thank you for using this program! Now exiting...")
    sys.exit()


main()
