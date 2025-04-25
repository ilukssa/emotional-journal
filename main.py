import json
import datetime

notes_path = "entries/notes.json"

def load_data_from_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def dump_data_to_json(file_path, new_data):
    with open(file_path, "w") as f:
        json.dump(new_data, f)

def main():
    user_input = input("Как ваше настроение?")
    current_date = datetime.datetime.now().date()
    data = {str(current_date) : user_input}
    dump_data_to_json(notes_path, data)

if __name__ == "__main__":
    main()