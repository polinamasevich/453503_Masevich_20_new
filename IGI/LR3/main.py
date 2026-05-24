"""
Toolbox containing various tasks that operate on strings and numbers

Subject: IGI
Lab: 3 (standard  types, collections, functions and modules)
Version: 1.0
Author: Masevich Polina
Date: 20.03.2026
"""

import sys
import ui
import task1
import task2
import task3
import task4
import task5


def task_exit():
    """
    Task used for exiting the program
    """

    sys.exit(0)


tasks = [task_exit, task1.run, task2.run, task3.run, task4.run, task5.run]


def menu():
    """
    Main menu selector.

    Provides user with a list of tasks and allows to select one of them,
    after task is selected it is launched.
    """

    print()
    print("======================")
    res = ui.read_int(
        f"Enter task number (1-{len(tasks) - 1}) or 0 to exit: ",
        min=0,
        max=len(tasks) - 1,
    )
    tasks[res]()


if __name__ == "__main__":
    while True:
        menu()
