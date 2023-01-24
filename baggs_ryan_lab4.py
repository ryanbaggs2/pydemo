"""
Name: Baggs, Ryan     SDEV 300-6980    Date: 07/08/2022

Program performs matrix operations and generate hashed passwords using
different hashing algorithms.
"""
# For exit function.
import sys

# For hashing algorithms.
import hashlib as hl

# For matrices
import numpy as np

# For reading .csv files.
import pandas as pd

# Menu selection options.
MATRIX_OPS = 1
PASS_OPS = 2
EXIT = 0

# Pattern types.
PHONE_PATT = 0
ZIP_PATT = 1

# Matrix size information.
ROW_SIZE = 3
NUM_ROWS = 3

# Matrix operation selections.
ADD = 1
SUB = 2
MUL = 3
ELEM_BY_ELEM_MUL = 4

# Global variables for tracking phone number and zip code.
PHONE_NUM = None
ZIP_CODE = None


def main():
    """
    Main function.

    Prints a welcome statement and starts the menu selection process for the
    program.
    """
    print("Welcome, this program performs some matrix operations, and "
          "\npassword operations.")

    while True:
        # Print statement to user.
        print("\nPlease enter what you would like to do: ")

        # Print the menu to the user.
        print("Enter 1 to perform matrix operations.")
        print("Enter 2 to perform password operations.")
        print("Enter 0 to exit.")

        exec_menu_selection(get_num_input(EXIT, PASS_OPS))


def exec_menu_selection(selection):
    """
    Executes the menu selection (function) to perform the specified
    operation.

    :param selection: of the user.
    """

    # Perform the matrix operations.
    if selection == MATRIX_OPS:
        matrix_ops()

    # Perform the password operations.
    if selection == PASS_OPS:
        pass_ops()

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


def matrix_ops():
    """
    Gets the user's phone number and zip code, saves them, and performs
    matrix operations specified by user.
    """
    # Modify the global variables.
    global PHONE_NUM, ZIP_CODE

    # Check if there is already a phone number input.
    if PHONE_NUM is None:
        # No phone number, get the user's phone number and zip code.
        PHONE_NUM, ZIP_CODE = get_valid_nums()

    # Get the first matrix.
    print("\nMatrix one:")
    np_mat = get_matrix()

    # Print out the first matrix.
    print(f"Your first matrix is:\n{np_mat}")

    # Get the second matrix.
    print("\nMatrix two:")
    np_mat_2 = get_matrix()

    # Print out the second matrix.
    print(f"Your second matrix is:\n{np_mat_2}")

    # Print menu for the matrix operation.
    print("Select a matrix operation:")
    print("Enter 1 to add.")
    print("Enter 2 to subtract.")
    print("Enter 3 to multiply.")
    print("Enter 4 to element by element multiplication.")

    # Get the selection.
    selection = get_num_input(ADD, ELEM_BY_ELEM_MUL)

    # Create a 3x3 empty matrix.
    np_mat_solution = [[] * ROW_SIZE] * NUM_ROWS

    # Initialize variable.
    operation = None

    # Check if the selection is Add.
    if selection == ADD:
        # Perform add operation, and update operation.
        np_mat_solution = np_mat + np_mat_2
        operation = "addition"

    # Check if the selection is Subtract.
    if selection == SUB:
        # Perform subtract operation, and update operation.
        np_mat_solution = np_mat - np_mat_2
        operation = "subtraction"

    # Check if the selection is Multiply.
    if selection == MUL:
        # Perform multiply operation, and update operation.
        np_mat_solution = np.matmul(np_mat, np_mat_2)
        operation = "multiplication"

    # Check if the selection is Element by Element Multiplication.
    if selection == ELEM_BY_ELEM_MUL:
        # Loop through the array left to right, top to bottom.
        for i in range(0, NUM_ROWS):
            for j in range(0, ROW_SIZE):
                # Multiply the individual elements.
                np_mat_solution[i][j] = np_mat[i][j] * np_mat_2[i][j]

        # Update operation.
        operation = "element by element multiplication"

    # Get the transpose of the matrix solution.
    np_mat_transpose = np_mat_solution.transpose()

    # Get the mean for each row.
    row_mean = np_mat_solution.mean(1)

    # Get the mean for each column.
    col_mean = np_mat_solution.mean(0)

    # Print the operation performed and the solution.
    print(f"\nYou selected: {operation}, the solution is: \n{np_mat_solution}")

    # Print the transpose of the solution.
    print(f"\nThe transpose is: \n{np_mat_transpose}")

    # Print the mean of the rows and columns.
    print(f"\nThe mean for each row is: {row_mean}")
    print(f"\nThe mean for each column is: {col_mean}")


def get_valid_nums():
    """
    Get the valid phone number and zip code.

    :return: the validated phone number and zip code.
    """
    return validate_pattern(PHONE_PATT), validate_pattern(ZIP_PATT)


def validate_pattern(pattern_type):
    """
    Validates the input against a specific pattern.

    :param pattern_type: to validate the input against.
    :return: the valid user input.
    """
    # Initialize the pattern to match.
    pattern = None

    # Check which pattern type to match.
    if pattern_type == PHONE_PATT:
        # Phone pattern.
        pattern = r"[0-9][0-9][0-9][-][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"
    elif pattern_type == ZIP_PATT:
        # Zip code pattern.
        pattern = r"[0-9][0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"

    # Initialize the valid flag.
    valid = False

    # Initialize variable.
    user_input = None

    # Loop until valid input received.
    while not valid:
        # Check the pattern type.
        if pattern_type == PHONE_PATT:
            # Get the user input.
            user_input = input("Please enter your phone number in format (xxx-xxx-xxxx):")
        elif pattern_type == ZIP_PATT:
            # Get the user input.
            user_input = input("Please enter your zip-code in format (xxxxx-xxxx)")

        # Check if the input matches the pattern and update the flag.
        valid = pd.Series(user_input).str.match(pattern)[0]

        # Check if flag is not valid.
        if not valid:
            # Inform user to match the formatting.
            print("Please match the specified formatting.")

    # Return the valid input.
    return user_input


def get_matrix():
    """
    Gets a 3x3 2d array from the user, validates it is correct size and
    contains only integers, and converts to a numpy 3x3 matrix.

    :return: The 3x3 numpy matrix.
    """
    # Print statement to user.
    print("Enter 3 values separated by a space, for each row:")

    # Initialize the 2d array.
    matrix_array = [[] * ROW_SIZE] * NUM_ROWS

    # Loop through each of the rows.
    for i in range(NUM_ROWS):
        # Loop until valid input received.
        while True:
            # Print the current row.
            print(f"Row {i + 1}")

            # Get the input from the user and split the values up.
            row = input().split()

            # Check that the length is 3.
            if len(row) != 3:
                # The user has not entered the correct size row, print
                # statement and continue loop.
                print("Must be 3 values.")
                continue

            # Throw error for any non-integer values, and continue while loop.
            try:
                # Loop through the values and cast them as integers.
                row = [int(j) for j in row]

            except ValueError:
                # Value is not an integer, throw an error and continue while
                # loop.
                print("All values must be integers.")
                continue

            # Valid input received.
            break

        # Add the current row to the 2d array.
        matrix_array[i] = row

    # Create a numpy matrix from the 2d array.
    np_mat = np.asmatrix(matrix_array)

    # Return the matrix.
    return np_mat


def pass_ops():
    """
    Gets a message from the user, encrypts the message using specified
    hashing algorithms, and prints out the encrypted message in hexadecimal.
    """
    # Print statement.
    print("Password operations: ")

    # Get the message from the user.
    message = input("Please enter a message that you would like to encode:\n")

    # Change the message to the codec format being used.
    message = message.encode()

    # Print the message hashed with md5 algorithm.
    print("md5:")
    print(hl.md5(message).hexdigest())

    # Print the message hashed with sha256 algorithm.
    print("sha256:")
    print(hl.sha256(message).hexdigest())

    # Print the message hashed with sha512 algorithm.
    print("sha512:")
    print(hl.sha512(message).hexdigest())


def exit_program():
    """ Prints an exit statement and exits program."""
    print("Thank you for using this program! Now exiting...")
    sys.exit()


main()
