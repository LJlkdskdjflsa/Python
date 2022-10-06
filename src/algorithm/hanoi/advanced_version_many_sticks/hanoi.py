# pyright: strict
"""hanoi tower question"""

from typing import List


def hanoi(n: int, sticks: List[str], from_stick: int, to_stick: int) -> int:
    """hanoi tower question
    when there are n plates and m sticks you have to move from one to another then the step is
    1. move n-(m-2) plates from one to another
    2. move the last (m-3) plates to random sticks
    3. move the last plates to the target stick
    4. move the last (m-3) on random sticks to the target stick
    5. move n-(m-2) plates to the target stick

    Args:
        n (int): the number of plates
        a (str): the stick name
        b (str): the stick name
        c (str): the stick name

    Returns:
        int: total times to move
    """
    if from_stick > len(sticks) - 1 or to_stick > len(sticks) - 1:
        raise ValueError
    move_counts: int = 0

    if n > 0:  # ending condition
        move_counts += hanoi(n - (len(sticks) - 2), a, c, b)
        print(f"moving from {a} to {c}")
        move_counts += 1
        move_counts += hanoi(n - 1, b, a, c)

    return move_counts


print(hanoi(3, "A", "B", "C"))
