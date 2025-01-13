"""
Additional program to covert data in Excel to JSON
"""


import pandas as pd
from IPython.display import display
import json
import os
import pathlib

current_file_folder_path = pathlib.Path(__file__).parent.resolve()
print(current_file_folder_path)

morse_dataframe = pd.read_excel("morse.alphabet.onecolumn.xlsx")

morse_dataframe["key"] = morse_dataframe["Sign"].str.get(0)

morse_dataframe = morse_dataframe.rename(columns={"Morse Code":"morse_code"})
display(morse_dataframe)

morse_frame_narrowed = morse_dataframe[["key","morse_code"]]
display(morse_frame_narrowed)
morse_json_noformat = morse_frame_narrowed.to_json(orient="records",force_ascii=False)

parsed = json.loads(morse_json_noformat)

morse_json_format= json.dumps(parsed, indent=4,ensure_ascii=False)
print(morse_json_format)


file_name = os.path.join(current_file_folder_path,"morse_code.json")

with open(file_name,"w",encoding="utf-8") as file:
    file.write(morse_json_format)

