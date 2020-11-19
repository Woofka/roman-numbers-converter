class Solution:
    NUMERALS_R2A = {
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

    VALID_SYMBOLS = 'IVXLCDM'

    def romanToInt(self, s: str) -> int:
        if not isinstance(s, str):
            raise TypeError("Argument must have type 'str'")

        if not 1 <= len(s) <= 15:
            raise ValueError("String must have length in range from 1 to 15 symbols")

        s = s.upper()

        if not self._is_valid(s):
            raise ValueError(f"String must only consist of symbols '{self.VALID_SYMBOLS}'")

        result = 0
        i = 0
        for roman, arabic in self.NUMERALS_R2A.items():
            while True:
                if s.find(roman, i, i+len(roman)) == -1:
                    break

                result += arabic
                i += len(roman)

                if i >= len(s):
                    break

        return result

    @classmethod
    def _is_valid(cls, s: str) -> bool:
        # TODO: Check for valid sequences
        valid = True
        for symbol in s:
            if symbol not in cls.VALID_SYMBOLS:
                valid = False
                break
        return valid


if __name__ == '__main__':
    tests = [
        ('I', 1),
        ('III', 3),
        ('IV', 4),
        ('IX', 9),
        ('LVIII', 58),
        ('MCMXCIV', 1994),
        ('MMMCMXCIX', 3999)
    ]

    solution = Solution()
    for test, expected_result in tests:
        returned_result = solution.romanToInt(test)
        if returned_result == expected_result:
            status = 'PASS'
        else:
            status = 'FAIL'
        print(f'[{status}] Test: {test}. Result: {returned_result}. Expected: {expected_result}')
