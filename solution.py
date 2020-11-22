import re


class Solution:
    # Roman numbers and their Arabic counterparts used in conversion
    NUMBERS_R2A = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    def romanToInt(self, s: str) -> int:
        """
        Return an Arabic number equal to Roman one.

        s: str - Roman number in range from I to MMMCMXCIX (from 1 to 3999)

        Raise TypeError if 's' is not a str.

        Raise ValueError if 's' is not a valid Roman number.
        """
        if not isinstance(s, str):
            raise TypeError("Argument must have type 'str'")

        s = s.upper()

        if not self._is_valid(s):
            raise ValueError(f"String must be a valid Roman number from I to MMMCMXCIX (from 1 to 3999)")

        result = 0
        i = 0
        # Iterating from higher numbers to lower numbers
        for roman, arabic in self.NUMBERS_R2A.items():
            while True:
                if s.find(roman, i, i+len(roman)) == -1:
                    break

                result += arabic
                i += len(roman)

                if i >= len(s):
                    break

        return result

    @staticmethod
    def _is_valid(s: str) -> bool:
        """
        Return True if 's' is a valid Roman number,
        return False otherwise.
        """
        # 15 is max possible length of Roman number in range from 1 to 3999
        if not 1 <= len(s) <= 15:
            return False

        # regexp from https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch06s09.html
        re_result = re.fullmatch(r'^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$', s)
        if re_result:
            return True
        return False


if __name__ == '__main__':
    tests = [
        # ('', None),       # Raises ValueError
        # ('a', None),      # Raises ValueError
        # (1, None),        # Raises TypeError
        # ('IIII', None),   # Raises ValueError
        ('I', 1),
        ('III', 3),
        ('IV', 4),
        ('IX', 9),
        ('LVIII', 58),
        ('MCMXCIV', 1994),
        ('MMMDCCCLXXXVIII', 3888),
        ('MMMCMXCIX', 3999),
    ]

    solution = Solution()
    for test, expected_result in tests:
        returned_result = solution.romanToInt(test)
        if returned_result == expected_result:
            status = 'PASS'
        else:
            status = 'FAIL'
        print(f'[{status}] Test: {test}. Result: {returned_result}. Expected: {expected_result}')
