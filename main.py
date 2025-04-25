import json
import datetime

notes_path = "entries/notes.json"

def load_data_from_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def dump_data_to_json(file_path, new_data):
    with open(file_path, "a") as f:
        json.dump(new_data, f, indent=2)

def main():


if __name__ == "__main__":
    main()