import sys
from RomanNumbersConverter import Converter


def main():
    if len(sys.argv) <= 1:
        print('No arguments. You should specify a Roman number to convert')
        return

    number = sys.argv[1]
    try:
        print(Converter.roman_to_int(number))
    except Exception:
        print('Wrong argument. Only Roman numbers from I to MMMCMXCIX (from 1 to 3999) are accepted for conversion')


if __name__ == '__main__':
    main()
