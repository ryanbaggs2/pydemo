"""
Performs the menu operations for the program.
"""
# For exit function.
import sys

# All menu's option.
EXIT = 0

# Main menu options.
MATRIX_OPS = 1
PASS_OPS = 2
STATE_INFO = 3


def main():
    """
    Main function.

    Prints a welcome statement and starts the menu selection process for the
    program.
    """
    print("Welcome to PyDemo, a program demonstrating some of the programming "
          "skills I have learned")

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
    if selection == MATRIX_OPS:
        matrix_ops()

    if selection == PASS_OPS:
        pass_ops()

    if selection == STATE_INFO:
        state_info()

    if selection == EXIT:
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


def pass_ops():
    """
    Requests user to log in, validating the credentials. After log in allows
    encoding of a message.
    """


def state_info():
    """
    Perform different US state information operations.

    Displays menu of options to: display the state, its capital, population,
    and flower, or modify the state population; search for a specific state's
    info; display the top 5 states by population; or update a specific state's
    population.
    """


def exit_program():
    """ Prints an exit statement and exits program."""
    print("Thank you for using this program! Now exiting...")
    sys.exit()


main()
