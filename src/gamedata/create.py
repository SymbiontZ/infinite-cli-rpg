import time, json, os
from utils.extra import clear
from utils.constants.localdir import DATA_DIR
from constants.difficulty import DIFF_SELECT_MSG
from constants.options import DIFF_OPTS
from gamedata.layout.save_file import new_savefile_dict

def new_save(saveDir: str = None):
    '''Makes a new save file'''
    if saveDir is None:
        saveDir = os.path.join(DATA_DIR,"save_0.json")

    with open(saveDir, "w") as savefile:
        savefile.write("")
    
    print("No se encontró ningun archivo de guardado, creando uno nuevo...")
    time.sleep(3)
    init_save(saveDir)


def init_save(saveDir: str):
    char_name = None
    difficulty = None

    while char_name is None or not len(char_name) > 0:
        clear()
        char_name = input("Escriba el nombre de su personaje: ")
    
    while difficulty not in DIFF_OPTS or difficulty is None:
        clear()
        try:
            difficulty = int(input(DIFF_SELECT_MSG))
        except ValueError:
            difficulty = None

    # DATA TO DICT AND SAVE IT INTO JSON FILE #
    
    saveFile_dict = new_savefile_dict()
    json_gameData = json.dumps(saveFile_dict, indent=4)
    with open(saveDir, "w") as saveFile:
        saveFile.write(json_gameData)