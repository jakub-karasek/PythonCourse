#!/usr/bin/env python3
import sys
from math import gcd

class Fraction:
    # Wersja2 __slots__ = ('numerator', 'denominator')  # ODKOMENTUJEMY WERSJI 2
    def __init__(self, numerator, denominator):
        assert denominator != 0
        self.numerator = int(numerator / gcd(numerator, denominator))
        self.denominator = int(denominator / gcd(numerator, denominator))

    def _simplify(self):
        temp = gcd(self.numerator, self.denominator)
        self.numerator //= temp
        self.denominator //= temp

    def __add__(self, other):
        new_denominator = (abs(self.denominator * other.denominator) //
                           gcd(self.denominator, other.denominator))
        new_numerator = (self.numerator * (new_denominator // self.denominator) +
                         other.numerator * (new_denominator // other.denominator))
        result = Fraction(new_numerator, new_denominator)
        result._simplify()
        return result
    
    def __sub__(self, other):
        new_denominator = (abs(self.denominator * other.denominator) //
                           gcd(self.denominator, other.denominator))
        new_numerator = (self.numerator * (new_denominator // self.denominator) -
                         other.numerator * (new_denominator // other.denominator))
        result = Fraction(new_numerator, new_denominator)
        result._simplify()
        return result

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result._simplify()
        return result

    def __truediv__(self, other):
        assert other.numerator != 0
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        result = Fraction(new_numerator, new_denominator)
        result._simplify()
        return result

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

def main():
    if len(sys.argv) < 3:
        print("Użycie: python version1.py n k")
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])

    fractions = [Fraction(1, 1) for _ in range(n)]

    for i in range(k):
        index = i % n
        next_index = (i+1) % n
        fractions[index] = fractions[index] + fractions[next_index]

    print("Przykładowe elementy:", fractions[0], fractions[-1])

if __name__ == "__main__":
    main()