from utils.gameData import load_saves
from utils.utils import clear

def start_game():
    clear()
    saveFiles = load_saves()
    print(saveFiles)













if __name__ == "__main__":
    start_game()