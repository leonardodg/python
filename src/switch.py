"""Module providing a function printing switch case in disc"""

from collections.abc import Callable


def case_1() -> None:
    """Function printing case 1"""
    print('case1')


def case_2() -> None:
    """Function printing case 2"""
    print('case2')


def case_default() -> None:
    """Function printing case default"""
    print('default')


RunCase = Callable[[], None]

switch: dict[str, RunCase] = {
    "1": case_1,
    "2": case_2,
}

if __name__ == "__main__":
    switch.get("2", case_default)()
