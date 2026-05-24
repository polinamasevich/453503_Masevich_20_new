import ui
import math


def generate_row(x):
    """
    Generator of members of approximation

    Args:
        x (float): argument of approximated function
    """

    n = 0
    xmult = x
    while True:
        yield (n, 2 * (1 / ((2 * n + 1) * xmult)))
        xmult *= x**2
        n += 1


NANO_EPS = 1e-9


def emit_table(x_val, eps_val, f_val):
    """
    Generator of rows for table displaying approximation computation

    Args:
        x_val (float): argument of approximated function
        eps_val (float): required precision
        f_val (float): value of approximated function
    """

    sum_val = 0
    for n, row_val in generate_row(x_val):
        sum_val += row_val
        eps_cur = abs(f_val - sum_val)
        yield (x_val, n, f_val, sum_val, eps_cur)
        if eps_cur < eps_val:
            break


def run():
    """
    Main runner of first task, requests inputs from user
    runs row approximation and displays result in form of table
    """

    x_val = ui.read_float(
        "Enter x (-inf to -1) or (1 to inf): ",
        ranges=[(-math.inf, -1 - NANO_EPS), (1 + NANO_EPS, math.inf)],
    )
    eps_val = ui.read_float("Enter eps (0 to 1): ", min=NANO_EPS, max=1)

    f_val = math.log((x_val + 1) / (x_val - 1))
    ui.show_table(emit_table(x_val, eps_val, f_val), ["x", "n", "f(x)", "sum", "eps"])
