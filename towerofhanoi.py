""" THE TOWER OF HANOI, by Frugal Jerk h.sapiens@hotmail.com
A stack-moving puzzle game. Credit: Al Sweigart """

import copy
import sys


TOTAL_DISKS = 5  # difficulty increases with increasing disks


COMPLETED_TOWER = list(range(TOTAL_DISKS, 0, -1))
towers = {"A": copy.copy(COMPLETED_TOWER), "B": [], "C": []}


def main():
    """Runs a single game of The Tower of Hanoi"""
    print(
        """THE TOWER OF HANOI, by Frugal Jerk h.sapiens@hotmail.com

Move the tower of disks, one disk at a time, to another tower. Larger
disks cannot rest on top of a smaller disk.

More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""
    )

    """The towers dictionary has keys "A", "B", and "C" and values
    that are lists representing a tower of disks. The list contains
    integers representing disks of different sizes, and the start of
    the list is the bottom of the tower. For a game with 5 disks,
    the list [5, 4, 3, 2, 1] represents a completed tower. The blank
    list [] represents a tower of no disks. The list [1, 3] has a
    larger disk on top of a smaller disk and is an invalid
    configuration. The list [3, 1] is allowed since smaller disks
    can go on top of larger ones."""

    while True:  # Run a siggle turn on each iteration of this loop.
        # display towers and disks at initial stage and promp
        display_towers(towers)

        # prompt user for input
        fromTower, toTower = get_input()

        # move disks from fromTower to toTower
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # check if new tower is completed in tower B or C
        if COMPLETED_TOWER in (towers["B"], towers["C"]):
            display_towers(towers)
            print("You Won")
            sys.exit()


def get_input():
    """Asks the player for a move. Returns (fromTower, toTower)."""

    while True:  # keep asking player until they enter a valid move.
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print("(e.g., AB to moves a disk from tower A to tower B.)")
        print()
        playermove = input(">").upper().strip()

        if playermove == "QUIT":
            print("Thank you for playing. Exiting game...")
            sys.exit()

        # Make sure the user enter valid tower letters:
        if playermove not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Invalid move. Enter one of AB, AC, BA, BC, CA, or CB.")
            continue  # Ask player again for their move.

        # Use more descriptive variable names:
        fromTower, toTower = playermove[0], playermove[1]

        if len(towers[fromTower]) == 0:
            # The 'from' tower cannot be an empty tower:
            print("Nothing to move from an empty tower")
            continue  # Ask player again for their move.
        elif len(towers[toTower]) == 0:
            # Any disk can be moved onto an empty "to" tower:
            return fromTower, toTower

        elif towers[fromTower][-1] > towers[toTower][-1]:
            print("Invalid move. Larger disk can not go on top of smaller disk")
            continue  # Ask player again for their move.
        else:
            # This is a valid move. so return the selected towers:
            return fromTower, toTower


def display_towers(towers):
    """Display the three towers with their disks."""

    # Display the three towers:
    emptyspace = " " * TOTAL_DISKS
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disks(0)  # Display the bare pole with no disk.
            else:
                display_disks(tower[level])  # Display the disk
        print()

    # Print tower labels ie A, B, and C:
    print(
        f"{emptyspace}A{emptyspace}{emptyspace} B{emptyspace}{emptyspace} C{emptyspace}\n"
    )


def display_disks(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    emptyspace = " " * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk:
        print(f"{emptyspace}||{emptyspace}", end="")
    else:
        # Display the disk:
        print(f'{emptyspace}{"@"*width}_{width}{"@"*width}{emptyspace}', end="")


# Optional features to implement for player to choose number of disks.
# def difficulty_level():
#     """Prompt user to enter a difficulty level from 3 (easiest) to 10 (expert)"""
#     while True:
#         diskcount = int(input("Please enter number of disks from 3 to 10. Higher the disk count, harder the game:"))
#
#         if diskcount not in [i for i in range(3, 11)]:
#             print('Please enter an integer from 3 to 10.')
#             continue
#
#         return diskcount


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":

    main()
