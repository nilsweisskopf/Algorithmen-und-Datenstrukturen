
import sys
from math import floor, log10
from copy import deepcopy
import time


class Counter:
    """
    Counter represents a fixed length decimal counter with maximum digits at
    each position.
    """

    def __init__(self, max_digits: list[int]):
        """
        Initializes an empty counter for a given number of positive maximum
        digits.

        >>> counter = Counter([5, 9, 14, 1])
        >>> counter.digits()
        [0, 0, 0, 0]
        >>> counter = Counter([])
        >>> counter.digits()
        []
        """
        self.max_digits = max_digits
        self.list = [0 for i in range(0, len(max_digits))]

    def digits(self) -> list[int]:
        """
        Returns the digits of this counter as a list of ints including leading
        zero digits. To guard against outside manipulation the returned value
        is a copy.

        >>> counter = Counter([9, 4, 23, 2, 1])
        >>> counter.digits()
        [0, 0, 0, 0, 0]
        >>> counter.digits()[0] += 5  # test that digits() returns a copy
        >>> counter.digits()
        [0, 0, 0, 0, 0]
        >>> counter2 = Counter([1, 1, 1])
        >>> counter2.digits()
        [0, 0, 0]
        """
        return deepcopy(self.list)
        

    def increment(self):
        """
        Increments the counter starting at the rightmost digit. If a digit
        becomes larger than its max value, carrying is applied as usual (think
        of a classic mechanical counter such as in a car's mileage counter)

        >>> counter = Counter([1, 23, 2])
        >>> counter.digits()
        [0, 0, 0]
        >>> counter.increment()
        >>> counter.digits()
        [0, 0, 1]
        >>> counter.increment()
        >>> counter.digits()
        [0, 0, 2]
        >>> counter.increment()
        >>> counter.digits()
        [0, 1, 0]
        >>> counter.increment()
        >>> counter.digits()
        [0, 1, 1]
        >>> counter.increment()
        >>> counter.digits()
        [0, 1, 2]
        >>> counter.increment()
        >>> counter.digits()
        [0, 2, 0]
        >>> for n in range(138):
        ...     counter.increment()
        >>> counter.digits()
        [0, 0, 0]
        """
        for i in range(len(self.list) - 1, -1, -1):
            self.list[i] += 1
            if self.list[i] > self.max_digits[i]:
                self.list[i] = 0
            else:
                break


    def is_zero(self) -> bool:
        """
        Returns true if the value of the counter is zero (if all digits
        are zero)

        >>> counter = Counter([34, 23])
        >>> counter.is_zero()
        True
        >>> for _ in range(7):
        ...     counter.increment()
        >>> counter.is_zero()
        False
        >>> for _ in range(24 * 35 - 7):
        ...     counter.increment()
        >>> counter.is_zero()
        True
        """
        return True if sum(self.list) == 0 else False
        

    def as_str(self) -> str:
        """
        Returns the value of the counter as a string of fixed length with
        leading zeroes. Values are simply concatenated. Each digit should be
        padded by zeros so that its total string length is always
        floor(log_10(max_digit)) + 1. You can for example use the zfill()
        method on strings for that.

        >>> counter = Counter([9, 9])
        >>> counter.as_str()
        '00'
        >>> for _ in range(7):
        ...     counter.increment()
        >>> counter.as_str()
        '07'
        >>> for _ in range(35):
        ...     counter.increment()
        >>> counter.as_str()
        '42'
        >>> counter = Counter([9, 14])
        >>> counter.as_str()
        '000'
        >>> for _ in range(4):
        ...     counter.increment()
        >>> counter.as_str()
        '004'
        >>> for _ in range(10):
        ...     counter.increment()
        >>> counter.as_str()
        '014'
        >>> counter.increment()
        >>> counter.increment()
        >>> counter.as_str()
        '101'
        """
        res = ""
        for i in range(len(self.list)):
            digit = self.list[i]
            max_digit = self.max_digits[i]
            res += str(digit).zfill(floor(log10(max_digit)) + 1)
        return res

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: counter.py <max_digit> <max_digit> … <max_digit>")
        sys.exit(1)
    
    # Erhalte die digits aus der Kommandozentrale
    digits = [int(d) for d in sys.argv[1:]]
    counter = Counter(digits)
    print("\r" + counter.as_str(), end="")

    while True:
        counter.increment
        if counter.is_zero():
            break
        print("\r" + counter.as_str(), end="")
        time.sleep(0.1)
    print("")