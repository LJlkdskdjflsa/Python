# pyright: strict
"""claculate time decorator"""

from time import time
from typing import Callable, TypeVar, ParamSpec

T = TypeVar("T")
P = ParamSpec("P")

# A decorator that preserves the signature.
def calculate_time(func: Callable[P, T]) -> Callable[P, T]:
    """calculate_time

    Args:
        func (Callable[P, T]): the function to calculate time

    Returns:
        Callable[P, T]: return function
    """

    def warpper(*args: P.args, **kwargs: P.kwargs) -> T:
        t_1 = time()
        result = func(*args, **kwargs)
        t_2 = time()
        print(f"{func.__name__} running time:  {t_2 - t_1} seconds")
        return result

    return warpper
