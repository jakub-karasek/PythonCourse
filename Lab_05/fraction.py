from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        assert denominator != 0
        self.numerator = int (numerator / gcd(numerator, denominator))
        self.denominator = int (denominator / gcd(numerator, denominator))

    def _simplify(self):
        temp = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // temp
        self.denominator = self.denominator // temp

    def __add__(self, other):
        result = Fraction(1, 1)
        new_denominator = int(abs(self.denominator * other.denominator) /
                              gcd(self.denominator, other.denominator))
        result.numerator = self.numerator * int (new_denominator / self.denominator)
        result.numerator += other.numerator * int (new_denominator / other.denominator)
        result.denominator = new_denominator
        result._simplify()
        return result

    def __sub__(self, other):
        result = Fraction(1, 1)
        new_denominator = int(abs(self.denominator * other.denominator) /
                              gcd(self.denominator, other.denominator))
        result.numerator = self.numerator * int (new_denominator / self.denominator)
        result.numerator -= other.numerator * int (new_denominator / other.denominator)
        result.denominator = new_denominator
        result._simplify()
        return result

    def __mul__(self, other):
        result = Fraction(1, 1)
        result.numerator = self.numerator * other.numerator
        result.denominator = self.denominator * other.denominator
        result._simplify()
        return result

    def __truediv__(self, other):
        assert other.numerator != 0
        result = Fraction(1, 1)
        result.numerator = self.numerator * other.denominator
        result.denominator = self.denominator * other.numerator
        result._simplify()
        return result

    def __str__(self):
        return self.numerator.__str__() + " / " + self.denominator.__str__()

    def __repr__(self):
        return self.numerator.__str__() + " / " + self.denominator.__str__()



# Main function to handle argument parsing and processing
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
    main()  # Run the main function
