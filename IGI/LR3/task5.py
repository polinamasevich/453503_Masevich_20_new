import ui
import randrow

def find_sum_after_first_positive(ls):
    """
    Computes sum of number after first positive

    Args:
        ls (list): list of numbers
    """
    pos_sum = 0
    seen_pos = False
    for elem in ls:
        if seen_pos:
            pos_sum += elem

        if elem > 0:
            seen_pos = True

    return pos_sum


def run():
    """
    Main runner of third task, requests row of floats from user, finds
    absolutely smallest element (and its index), computes sum of number
    after first positive and displays results
    """

    ls = ui.read_float_list("Enter list (numbers separated by space) or enter positive integer to randomly init row: ")
    if int(ls[0]) > 0:
        ls = list(randrow.random_row(int(ls[0])))
        print("Generated random row: ", ls)

    smalles_idx, smallest = min(enumerate(ls), key=lambda x: abs(x[1]))

    print(f"Smallest abs element: {smallest}")
    print(f"Smallest abs element index: {smalles_idx}")

    pos_sum = find_sum_after_first_positive(ls)
    print(f"Sum after first positive element: {pos_sum}")
