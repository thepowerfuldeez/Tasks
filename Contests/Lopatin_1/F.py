import sys

sys.stdin = open("fraction.in")
sys.stdout = open("fraction.out", "w")

a, b = map(int, input().split())
# k = b // a
# r = b % a
#
# print("1/{}".format(k + 1))
# while r != 0:
#     a -= r
#     b *= k + 1
#     k = b // a
#     r = b % a
#     print("1/{}".format(k + 1))
# print("{}/{}".format(a - r, b * (k + 1)))


from fractions import Fraction


def greedyEgyptianFraction(rational):
    # Sanity check: the rational number should be in the range (0, 1)
    if rational <= 0 or rational >= 1:
        raise Exception("Rational number out of range" , rational)

    # Create a list to store the Egyptian fraction representation.
    result = []

    # Now, iteratively subtract out the largest unit fraction that may be
    # subtracted out until we arrive at a unit fraction.
    while True:
        # If the rational number has numerator 1, we're done.
        if rational.numerator == 1:
            result.append(rational)
            return result

        # Otherwise, find the largest unit fraction less than the current
        # rational number.  This is given by the ceiling of the denominator
        # divided by the numerator
        unitFraction = Fraction(1, rational.denominator // rational.numerator + 1)
        result.append(unitFraction)

        # Subtract out this unit fraction.
        rational = rational - unitFraction

res = greedyEgyptianFraction(Fraction(a, b))
for f in res:
    print(f)
