"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(number_of_layers):
    """Calculate the bake time remaining.

    Parameters:
        number_of_layers (int): The number of layers you want to add to the lasagna.

    Returns:
        int: The perparation time (in minutes)  Assume each layer takes 2 minutes to prepare.

    Function that takes the number_of_layers you want to add to the lasagna as an argument and 
    returns how many minutes you would spend making them, based on PREPARATION_TIME.
    """
    
    return PREPARATION_TIME * number_of_layers



#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time (in minutes).

    Parameters:
        number_of_layers (int): The number of layers added to the lasagna.
        elapsed_bake_time (int): The number of minutes the lasagna has spent baking in the oven already.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function returns the total minutes you have been in the kitchen cooking — 
    your preparation time layering + the time the lasagna has spent baking in the oven.
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time