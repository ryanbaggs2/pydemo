"""
Name: Baggs, Ryan     SDEV 300-6980    Date: 07/20/2022

Python Data Analysis App prints data for population and housing, giving
options to select more specific columns of the data.
"""
# For exit function.
import sys

# For csv file reading.
import pandas as pd

# For math functions.
import numpy as np

# For histogram.
import matplotlib.pyplot as plt

# All menu's selection option.
EXIT = 0

# Main menu selection options.
POP_DATA = 1
HOUSE_DATA = 2

# Population menu selection options.
POP_APRIL = 1
POP_JUL = 2
CHANGE_POP = 3
EXIT_POP_COL = 4

# Housing menu selection options.
AGE = 1
BEDRMS = 2
BUILT = 3
ROOMS = 4
UTILITY = 5
EXIT_HOUSING_COL = 6


def main():
    """
    Main function.

    Prints a welcome statement and starts the menu selection process for the
    program.
    """
    print("Welcome to the Python Data Analysis App.")

    while True:
        # Print statement to user.
        print("\nPlease enter what you would like to do: ")

        # Print the menu to the user.
        print("Enter 1 to get population data.")
        print("Enter 2 to get housing data.")
        print("Enter 0 to exit.")

        exec_menu_selection(get_num_input(EXIT, HOUSE_DATA))


def exec_menu_selection(selection):
    """
    Executes the menu selection (function) to perform the specified
    operation.

    :param selection: of the user.
    """

    # Perform the population data operations.
    if selection == POP_DATA:
        pop_data()

    # Perform the housing data operations.
    if selection == HOUSE_DATA:
        house_data()

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


def pop_data():
    """
    Prints the population data menu to the user, gets their input, and gets
    the column of data that was requested, or exits the population
    menu/program if selected.
    """
    # Print statement to user.
    print("\nYou have entered Population Data.")
    print("Please enter the column you would like statistics for: ")

    # Print the menu to the user.
    print("Enter 1 for column Pop Apr 1")
    print("Enter 2 for column Pop Jul 1")
    print("Enter 3 for column Change Pop")
    print("Enter 4 to exit column")
    print("Enter 0 to exit App.")

    # Get the user selection.
    selection = get_num_input(EXIT, EXIT_POP_COL)

    # Initialize the column title.
    col_title = None

    # Update col_title to corresponding selection, exit the column, or
    # exit program.
    if selection == POP_APRIL:
        col_title = "Pop Apr 1"
    elif selection == POP_JUL:
        col_title = "Pop Jul 1"
    elif selection == CHANGE_POP:
        col_title = "Change Pop"
    elif selection == EXIT_POP_COL:
        return
    elif selection == EXIT:
        exit_program()

    load_and_print("PopChange.csv", col_title)


def house_data():
    """
    Prints the housing data menu to the user, gets their input, and gets
    the column of data that was requested, or exits the housing
    menu/program if selected.
    """
    # Print statement to user.
    print("\nYou have entered Housing Data.")
    print("Please enter the column you would like statistics for: ")

    # Print the menu to the user.
    print("Enter 1 for column AGE")
    print("Enter 2 for column BEDRMS")
    print("Enter 3 for column BUILT")
    print("Enter 4 for column ROOMS")
    print("Enter 5 for column UTILITY")
    print("Enter 6 to exit column")
    print("Enter 0 to exit App.")

    # Get the user selection.
    selection = get_num_input(EXIT, EXIT_HOUSING_COL)

    # Initialize the column title.
    col_title = None

    # Update col_title to corresponding selection, exit the column, or
    # exit program.
    if selection == AGE:
        col_title = "AGE"
    elif selection == BEDRMS:
        col_title = "BEDRMS"
    elif selection == BUILT:
        col_title = "BUILT"
    elif selection == ROOMS:
        col_title = "ROOMS"
    elif selection == UTILITY:
        col_title = "UTILITY"
    elif selection == EXIT_POP_COL:
        return
    elif selection == EXIT:
        exit_program()

    load_and_print("Housing.csv", col_title)


def load_and_print(file_name, col_title):
    """
    Loads and prints the specified file and column to the console as well as
    displays a histogram for the user to analyze.

    :param file_name: String of the name of the file to load, must include
    the .csv filetype.
    :param col_title: String of the column title in the .csv file to get
    the data from.
    """
    # Try to load the file.
    try:
        # Load the data from the CSV file.
        data_frame = pd.read_csv("../week5/" + file_name)

        # Try to get the specified column.
        try:
            # Get the specified column from the data as a numpy array.
            column = np.asarray(data_frame[col_title])

            # Calculate the different statistics.
            count = column.size
            mean = column.mean()
            std_dev = column.std()
            minimum = np.min(column)
            maximum = np.max(column)

            # Create the histogram.
            plt.hist(column, "auto")

            # Print the results.
            print(f"\nHere is the information from column: {col_title}")
            print(f"Count: {count}")
            print(f"Mean: {mean:.1f}")
            print(f"Standard Deviation: {std_dev:.1f}")
            print(f"Min: {minimum}")
            print(f"Max: {maximum}")
            print("Histogram:\n")

            # Display the histogram.
            plt.show()
        except KeyError:
            # The specified column was not found, print an error.
            print("This column is not found in the .csv file.")

    except FileNotFoundError as e:
        # The file was not found, print an error message.
        print("File was not found.")
        print(e)


def exit_program():
    """ Prints an exit statement and exits program."""
    print("Thank you for using this program! Now exiting...")
    sys.exit()


main()
