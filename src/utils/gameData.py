import json, os, time
from utils.utils import clear
from constants.localdir import DATA_DIR
from layout.prompts import save_file_join

def load_saves() -> list:
    '''
    Searches on your directory in order to find save files.

    If there is no save file, make a new one.
    '''

    saved_games = []        #List with the name of save files

    # Checks if there is any path to save game #
    # If not, it creates one, otherwise stores in a list path of save files #
    if not os.path.exists(DATA_DIR):           
        os.mkdir(DATA_DIR)
    
    while len(saved_games) == 0:
        saved_games = os.listdir(DATA_DIR)

        if len(saved_games) == 0:
            new_save(save_file_join("save_0.json"))
            saved_games.append("save_0,json")
            pass

    return saved_games

def new_save(saveDir: str):
    '''Makes a new save file'''
    with open(saveDir, "w") as savefile:
        savefile.write("")
    
    print("No se encontró ningun archivo de guardado, creando uno nuevo...")
    time.sleep(3)
    create_save(saveDir)

def create_save(saveDir: str) -> json:
    char_name = None
    difficulty = None

    while char_name is None or not len(char_name) > 0:
        clear()
        char_name = input("Escriba el nombre de su personaje: ")
    
    while difficulty is None or (difficulty < 1  or difficulty > 4):
        clear()
        try:
            difficulty = int(input())
        except ValueError:
            difficulty = None

    # DATA TO DICT AND SAVE IT INTO JSON FILE #
    saveFile_dict = {
        "name": char_name,
        "difficulty": difficulty,
        "level": 0,
        "stats": {
            "base": {
                "atk": 25
            },
            "gained": {

            }
        },
    }
    json_gameData = json.dumps(saveFile_dict, indent=4)
    with open(saveDir, "w") as saveFile:
        saveFile.write(json_gameData)