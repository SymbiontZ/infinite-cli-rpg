from gamedata.load import load_saves
from gamedata.create import new_save
from utils.extra import clear

def start_game():
    clear()
    saveFiles = load_saves()
    if len(saveFiles) == 0:
        new_save()

if __name__ == "__main__":
    start_game()