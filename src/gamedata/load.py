import os
from constants.localdir import DATA_DIR
from utils.gamedata import save_file_join

def load_saves() -> list:
    '''
    Searches on your directory in order to find save files.
    '''

    saved_games = []        #List with the name of save files

    # Checks if there is any path to save game #
    # If not, it creates one, otherwise stores in a list path of save files #
    if not os.path.exists(DATA_DIR):           
        os.mkdir(DATA_DIR)

    saved_games = os.listdir(DATA_DIR)

    return saved_games