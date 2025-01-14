"""
Additional program to covert data in Excel to JSON
Read data from folder in which this script is located
from file MORSE_CONVERSION_DATA_XLS.
Created result JSON called MORSE_CODE_JSON
"""

import json
import os
import pathlib

import pandas as pd
from dotenv import load_dotenv

# noinspection PyUnresolvedReferences
from IPython.display import display  # Used for commented data display block # noqa: F401 

#Load constant from environment file
load_dotenv()
MORSE_CODE_JSON = os.getenv("MORSE_CODE_JSON")
MORSE_CODE_KEY_VALUE_JSON = os.getenv("MORSE_CODE_KEY_VALUE_JSON")
MORSE_CONVERSION_DATA_XLS = os.getenv("MORSE_CONVERSION_DATA_XLS")



def load_data_to_df(folder_path: str) -> pd.DataFrame:
    """Load data from Excel in const MORSE_CONVERSION_DATA_XLS
    and returns DataFrame in pandas format

    :param folder_path: source file folder
    :return: Morse conversion table in the form of Pandas.DataFrame
    """

    file_name = os.path.join(folder_path, MORSE_CONVERSION_DATA_XLS)

    morse_dataframe = pd.read_excel(file_name)
    morse_dataframe["key"] = morse_dataframe["Sign"].str.get(0)
    morse_dataframe = morse_dataframe.rename(columns={"Morse Code": "morse_code"})

    morse_frame_narrowed = morse_dataframe[["key", "morse_code"]]
    return morse_frame_narrowed


def get_current_folder() -> str:
    """Get current folder of script location
    :return: folder path
    """
    current_folder = pathlib.Path(__file__).parent.resolve()
    return str(current_folder)


def to_json_key_value(folder_path: str, morse_data_df: pd.DataFrame):
    """Export Morse Conversion data to json in following format \n
    [
        {
            "key": "A",
            "morse_code": "•-"
        }, \n
        {
            "key": "B",
            "morse_code": "-•••"
        }
    ] \n
    where: key is string, morse_code is representation sign in Morse Code


    :param folder_path: source file and data folder
    :param morse_data_df: pandas.DataFrame with Morse Conversions
    """

    morse_json_noformat = morse_data_df.to_json(orient="records", force_ascii=False)
    parsed = json.loads(morse_json_noformat)
    morse_json_format = json.dumps(parsed, indent=4, ensure_ascii=False)
    # Check how to be json looks like
    print("Morse conversion table json format:")
    print(morse_json_format)
    save_json(folder_path, MORSE_CODE_KEY_VALUE_JSON,morse_json_format)



def to_json(folder_path: str, morse_data_df: pd.DataFrame):
    """Export Morse Conversion data to json in following format \n
    {
        "A": "•-",
        "B": "-•••",
    }
    :param folder_path: source file and data folder
    :param morse_data_df: pandas.DataFrame with Morse Conversions
    """

    morse_dict = { row["key"]: row["morse_code"] for (index, row) in morse_data_df.iterrows()}
    json_string = json.dumps(morse_dict, indent=4, ensure_ascii=False)

    # Check how to be json looks like
    print("Morse conversion table json format:")
    print(json_string)

    save_json(folder_path, MORSE_CODE_JSON,json_string)


def save_json(folder_path, file_name:str, json_string:str):
    """Saves string JSON format to file

    :param folder_path: target save folder
    :param file_name: file name of json file
    :param json_string: json string to be saved
    """

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(json_string)


def main():
    folder_path = get_current_folder()
    morse_data_df = load_data_to_df(folder_path)

    # Check how df looks like
    # print("Morse conversion table in pandas format:")
    # display(morse_data_df)

    to_json_key_value(folder_path, morse_data_df)
    to_json(folder_path, morse_data_df)

if __name__ == '__main__':
    main()

