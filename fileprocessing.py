import json
import os


class FileProcessing:
    def load_month_data():
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        return data


    def store_month_data(month_data):
        with open("data.json", "w") as file:
            json.dump(month_data, file, indent=4)


    def delete_all_entries():
        if os.path.exists("data.json"):
            os.remove("data.json")


