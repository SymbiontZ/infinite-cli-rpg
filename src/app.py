from gamedata.load import load_saves
from interface.principals import main_menu
 
def main():
    save_files = load_saves()
    main_menu(save_files)
    exit()

if __name__ == "__main__":
    main()