"""
Project from Day 82 of Udemy course "100 Days of Python"
Conversion of string to Morse code: https://en.wikipedia.org/wiki/Morse_code
Polish letters included: https://pl.wikipedia.org/wiki/Kod_Morse%E2%80%99a
"""

import json
import sys

MORSE_CODE_JSON = "data/morse_code.json"


def load_json(path: str) -> dict[str, str]:
    """Loads Json file from path with String to Morse code conversion rules
    Returns dictionary with data from Json.

    :param path: Path to file
    :return: dictionary with conversion rules
    """

    data: dict[str, str]
    with open(path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def encode_to_morse(string: str, conversion_dict: dict[str, str]):
    """Encodes strings in Morse Code

    :param string: string to be encoded
    :param conversion_dict: dictionary with conversions
    """

    print(f"Source string:\n{string}")
    try:
        morse_list = [encoder(char, conversion_dict) for char in string.upper()]
        # print(f"Morse result list: {morse_list}")
        morse_string = "".join(morse_list)
        print(f"Morse result:\n{morse_string}")
    except KeyError as err:
        error_msg = str(err)
        sys.exit(f"Error occurred:  Char {error_msg} is not supported.")


def encoder(char: str, conversion_dict: dict[str, str]) -> str:
    """Encodes char in Morse Code

    :param char: char to encode
    :param conversion_dict: dictionary with conversions
    :raises: KeyError with not supported character
    :return: converted Morse code
    """

    if char == "\n":
        return char
    return "{} ".format(conversion_dict[char])


def main():
    loaded_dict = load_json(MORSE_CODE_JSON)
    # print(loaded_dict)
    encode_to_morse("Mama ma kota\nSOS\nYEAH!", loaded_dict)
    encode_to_morse("An exception has occurred!~", loaded_dict)


if __name__ == '__main__':
    main()

# TODO Add decode
