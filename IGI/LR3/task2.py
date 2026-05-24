import ui


def run():
    """
    Main runner of second task, requests inputs from user until
    positive number is entered. Computes row multiplication and
    displays result
    """

    xv = 0
    mult = 1
    while xv <= 0:
        xv = ui.read_int("Enter number (to finish enter positive one): ")
        mult *= xv

    print(f"Result: {mult}")
