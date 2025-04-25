import json
import datetime

notes_path = "entries/notes.json"

def load_data_from_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def dump_data_to_json(file_path, new_data):
    with open(file_path, "w") as f:
        json.dump(new_data, f, indent=2)

def get_user_input():
    data = load_data_from_json(notes_path)
    to_rewrite = "y"
    user_input = input()
    current_date = str(datetime.datetime.now().date())
    if current_date in data:
        to_rewrite = input("Вы уже оставляли сегодня запись, хотите переписать? (yY/nN): ").lower()
        while to_rewrite != "y" and to_rewrite != "n":
            to_rewrite = input("Введите (yY/nN): ").lower()
    if to_rewrite == "y":
        data[current_date] = user_input
        dump_data_to_json(notes_path, data)

def main():
    get_user_input()


if __name__ == "__main__":
    main()