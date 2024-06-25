import os
from constants.paths import DATA_PATH

def load_saves() -> list[str]:
    '''
    Searches on your directory in order to find save files.
    '''

    saved_games = []        #List with the name of save files

    # Checks if there is any path to save game #
    # If not, it creates one, otherwise stores in a list path of save files #
    if not os.path.exists(DATA_PATH):           
        os.mkdir(DATA_PATH)

    saved_games = os.listdir(DATA_PATH)

    return saved_games


            