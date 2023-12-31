""" color_hw.py """

from typing import Union

from typing_extensions import Self


class Color:
    """Class that provides possibilty to print a colored circle"""

    START: str = "\033[1;38;2"
    MOD: str = "m"
    END: str = "\033[0"

    def __init__(self, r=0, g=0, b=0):
        self.r_val = r
        self.g_val = g
        self.b_val = b
        self.values = (self.r_val, self.g_val, self.b_val)

    def __repr__(self) -> str:
        return f"Color({self.r_val};{self.g_val};{self.b_val})"

    def __str__(self) -> str:
        return (
            f"{self.START};{self.r_val};{self.g_val};{self.b_val}"
            f"{self.MOD}●{self.END}{self.MOD}"
        )

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, type(self)):
            return self.values == __value.values
        return False

    def __add__(self, __value: object) -> Self:
        if isinstance(__value, type(self)):
            values = tuple(
                self.values[i] + __value.values[i] for i in range(3)
            )
            return self.__class__(*values)
        raise TypeError(
            "Argument '__value' has incompatible type:"
            " expected type 'TColor'"
            f", got '{type(__value).__name__}' instead."
        )

    def __hash__(self) -> int:
        return hash(self.values)

    def __mul__(self, c: Union[int, float]) -> Self:
        """
        Function to reduce contrast
        """
        if not isinstance(c, (int, float)):
            raise TypeError(
                f"'c' must be 'int' or 'float', not '{type(c).__name__}'"
            )

        if not 0 <= c <= 1:
            raise ArithmeticError("'c' must be between 0 and 1")

        cl = -256 * (1 - c)
        f = 259 / 255 * (cl + 255) / (259 - cl)

        self.values = tuple(int(f * (i - 128) + 128) for i in self.values)
        self.r_val, self.g_val, self.b_val = self.values
        return self


if __name__ == "__main__":
    red = Color(255, 0, 0)
    green = Color(g=255)
    blue = Color(b=255)

    second_red = Color(255, 0, 0)
    print(red, green, blue, red != blue, red == second_red, red == green)

    print(red + green)

    try:
        print(red + 5)
    except TypeError:
        print("ok")

    print(set([red, green, blue, second_red]))

    print(red + green)
    print(((red + green) * 0.6))
