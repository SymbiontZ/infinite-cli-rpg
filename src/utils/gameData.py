import json, os, time

def load_saves() -> list:
    '''
    Searches on your directory in order to find save files.

    If there is no save file, make a new one.
    '''
    
    local_dir = os.getcwd()
    saved_games = []
    saved_dir = local_dir+"\\data"

    # Checks if there is any path to save game #
    # If not, it creates one, otherwise stores in a list path of save files #
    if not os.path.exists(saved_dir):           
        os.mkdir(saved_dir)
    else:
        saved_games = os.listdir(saved_dir)

    # Create new save file if there is no one #
    if len(saved_games) == 0:
        new_save(local_dir+"\\data\\save_0.json")
        saved_games.append("save_0,json") 


    return saved_games

def new_save(saveDir: str):
    '''Makes a new save file'''
    with open(saveDir, "w") as savefile:
        savefile.write("")
    
    print("No se encontró ningun archivo de guardado, creando uno nuevo...")
    time.sleep(3)
    create_save(saveDir)

def create_save(saveDir: str) -> json:
    char_name = input("Escriba el nombre de su personaje: ")



    # DATA TO DICT AND SAVE IT INTO JSON FILE #
    saveFile_dict = {
        "name": char_name
    }
    json_gameData = json.dumps(saveFile_dict, indent=4)
    with open(saveDir, "w") as saveFile:
        saveFile.write(json_gameData)