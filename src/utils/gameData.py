import os
from constants.localdir import DATA_DIR

def save_file_join(save_file_name:str) -> str:
    "Returns the path to a save file"
    return os.path.join(DATA_DIR,save_file_name) 