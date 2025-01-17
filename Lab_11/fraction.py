#!/usr/bin/env python3
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        assert denominator != 0, "Denominator cannot be zero."
        common_div = gcd(numerator, denominator)
        self.numerator = int(numerator // common_div)
        self.denominator = int(denominator // common_div)

    def _simplify(self):
        temp = gcd(self.numerator, self.denominator)
        self.numerator //= temp
        self.denominator //= temp

    def __add__(self, other):
        new_denominator = abs(self.denominator * other.denominator) // gcd(self.denominator, other.denominator)
        new_numerator = (self.numerator * (new_denominator // self.denominator) +
                         other.numerator * (new_denominator // other.denominator))
        result = Fraction(new_numerator, new_denominator)
        result._simplify()
        return result

    def __sub__(self, other):
        new_denominator = abs(self.denominator * other.denominator) // gcd(self.denominator, other.denominator)
        new_numerator = (self.numerator * (new_denominator // self.denominator) -
                         other.numerator * (new_denominator // other.denominator))
        result = Fraction(new_numerator, new_denominator)
        result._simplify()
        return result

    def __mul__(self, other):
        result = Fraction(self.numerator * other.numerator,
                          self.denominator * other.denominator)
        result._simplify()
        return result

    def __truediv__(self, other):
        assert other.numerator != 0, "Cannot divide by fraction with numerator = 0."
        result = Fraction(self.numerator * other.denominator,
                          self.denominator * other.numerator)
        result._simplify()
        return result

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def save_to_file(self, filename: str) -> None:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{self.numerator}/{self.denominator}")

    @classmethod
    def load_from_file(cls, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            num, den = content.split('/')
            return cls(int(num), int(den))


def main():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)

    f3 = f1 + f2
    print(f"({f1}) + ({f2}) = ({f3})")

    f3 = f1 - f2
    print(f"({f1}) - ({f2}) = ({f3})")

    f3 = f1 * f2
    print(f"({f1}) * ({f2}) = ({f3})")

    f3 = f1 / f2
    print(f"({f1}) / ({f2}) = ({f3})")


if __name__ == '__main__':
    main()