"""
Main functionality of the programm

@ilukssa 2025-04-25
"""
import json
import datetime

NOTES_PATH = "entries/notes.json"

def load_data_from_json(file_path):
    """Load data from JSON file

    Args:
        file_path (str): path to json

    Returns:
        dict: dict with data as key and note as value
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        return {}

def dump_data_to_json(file_path, new_data):
    """Dump data to JSON file

    Args:
        file_path (str): path to json
        new_data (dict): dict with data as key and note as value
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, indent=2)

def get_user_input():
    """Get user input and dump it to JSON file
    """
    data = load_data_from_json(NOTES_PATH)
    to_rewrite = "y"
    user_input = input()
    current_date = str(datetime.datetime.now().date())
    if current_date in data:
        to_rewrite = input("Вы уже оставляли сегодня запись, хотите переписать? (yY/nN): ").lower()
        while to_rewrite not in ("y", "n"):
            to_rewrite = input("Введите (yY/nN): ").lower()
    if to_rewrite == "y":
        data[current_date] = user_input
        dump_data_to_json(NOTES_PATH, data)

def main():
    """main
    """
    get_user_input()

if __name__ == "__main__":
    main()
