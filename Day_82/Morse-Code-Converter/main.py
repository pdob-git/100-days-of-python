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
    Display results

    :param string: string to be encoded
    :param conversion_dict: dictionary with conversions
    """

    print(f"Source string:\n{string}")

    try:
        morse_string = encode(conversion_dict, string)
        print(f"Morse result:\n{morse_string}")
        print()  # empty line to separate results
    except KeyError as err:
        error_msg = str(err)
        sys.exit(f"Error occurred:  Char {error_msg} is not supported.")


def encode(conversion_dict: dict[str, str], string: str) -> str:
    """Sub method for `encode_to_morse`
    Encodes strings in Morse Code

    :param conversion_dict:  dictionary with conversions
    :param string: string to be encoded
    :return: result of encoded string
    """

    encoded_list = ["{} ".format(encoder(char, conversion_dict)) for char in string.upper()]

    encoded_string = "".join(encoded_list)
    encoded_string = encoded_string.replace("\n ", "\n")
    return encoded_string



def decode(conversion_dict: dict[str, str], string: str) -> str:
    """Sub method for `decode_from_morse`
    Decodes strings from Morse Code

    :param conversion_dict:  dictionary with conversions
    :param string: string to be decoded
    :return: result of decoded string
    """

    # Add space ad the beginning of each line and preserve end of lines in list
    string = string.replace("\n","\n ")

    morse_codes_list = string.split(" ")
    morse_codes_no_empty = [char for char in morse_codes_list if char != '']

    encoded_list = [encoder(char, conversion_dict) for char in morse_codes_no_empty]
    encoded_string = "".join(encoded_list)
    return encoded_string



def encoder(char: str, conversion_dict: dict[str, str]) -> str:
    """Encodes char in Morse Code if provided conversion dictionary is in form
    {Sign: Morse_code}
    Decodes char from morse code if provided conversion dictionary is in form
    {Morse_code: Sign}

    :param char: char to encode
    :param conversion_dict: dictionary with conversions
    :raises: KeyError with not supported character
    :return: single character converted Morse code or Decoded from Morse Code
    """

    if char == "\n":
        return char
    return conversion_dict[char]


def decode_from_morse(morse_string: str, conversion_dict: dict[str, str]):
    """Decodes strings from Morse Code
    Display results

    :param morse_string: string to be decoded
    :param conversion_dict: dictionary with conversions
    """

    inverted_dict = {value: key for key, value in conversion_dict.items()}
    print(f"Morse string:\n{morse_string}")

    try:
        result_string = decode(inverted_dict, morse_string)
        print(f"Decoded result:\n{result_string}")
        print() #empty line to separate results
    except KeyError as err:
        error_msg = str(err)
        sys.exit(f"Error occurred:  Char {error_msg} is not supported.")


def main():
    loaded_dict = load_json(MORSE_CODE_JSON)
    # print(loaded_dict)
    encode_to_morse("Mama ma kota\nSOS\nYEAH!", loaded_dict)
    encode_to_morse("The joke was great!", loaded_dict)
    morse_one = r"""-- •- -- •- / -- •- / -•- --- - •- 
••• --- ••• 
-•-- • •- •••• -•-•-- """
    morse_two = r"""- •••• • / •--- --- -•- • / •-- •- ••• / --• •-• • •- - -•-•-- ~"""

    decode_from_morse(morse_one, loaded_dict)
    decode_from_morse(morse_two, loaded_dict)


if __name__ == '__main__':
    main()

# TODO Add decode
