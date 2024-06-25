import os
from constants.paths import DATA_PATH

def filename_to_filepath(save_file_name:str) -> str:
    "Returns the path to a save file"
    return os.path.join(DATA_PATH,save_file_name) 


def data_to_savefile_dict (name:str, difficulty:int) -> dict:
    save_file = {
        "name": f"{name}",
        "difficulty": int(f"{difficulty}"),
        "level": 0,
        "stats": {
            "base": {
                "hp": 100,
                "atk": 25,
                "def":25,
            },
            "gained": {
                "hp": 0,
                "atk": 0,
                "def": 0,
            },
        },
        "items": [],
    }
    return save_file


def save_list_to_save_dict(save_list):
    print("hola")