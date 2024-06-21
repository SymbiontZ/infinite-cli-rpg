import time, json, os
from constants.localdir import DATA_DIR
from constants.difficulty import DIFF_SELECT_MSG
from constants.options import DIFF_OPTS
from layout.save_file import new_savefile_dict
from utils.extra import clear

def new_save(saveName: str = None):
    '''Makes a new save file'''

    if saveName is None:
        saveName = os.path.join(DATA_DIR, "save_0.json")
    else:
        saveName = os.path.join(DATA_DIR, saveName)

    with open(saveName, "w") as savefile:
        savefile.write("")

    time.sleep(3)
    init_save(saveName)


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
    
    saveFile_dict = new_savefile_dict(name= char_name, difficulty= difficulty)
    print(saveFile_dict)
    json_gameData = json.dumps(saveFile_dict, indent=4)
    with open(saveDir, "w") as saveFile:
        saveFile.write(json_gameData)