# pyright: strict
"""hanoi tower question"""


def hanoi(n: int, a: str, b: str, c: str) -> int:
    """hanoi tower question
    when there are n plates and you have to move from a pass b to c, then the step is
    1. move n-1 plates from a pass c to b
    2. move the last plate from a to c
    3. move the n-1 plates from b pass a to c


    Args:
        n (int): the number of plates
        a (str): the stick name
        b (str): the stick name
        c (str): the stick name

    Returns:
        int: total times to move
    """
    move_counts: int = 0

    if n > 0:  # ending condition
        move_counts += hanoi(n - 1, a, c, b)
        print(f"moving from {a} to {c}")
        move_counts += 1
        move_counts += hanoi(n - 1, b, a, c)

    return move_counts


print(hanoi(3, "A", "B", "C"))
