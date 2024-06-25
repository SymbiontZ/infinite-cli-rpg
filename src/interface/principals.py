from utils.tools import clear,int_input, wait
from utils.validators import validate_games, validate_int_opt
from constants.options import MAIN_MENU_OPTS

def main_menu(save_files: list[str]):
    opt = None
    while opt is None or opt != 0:
        clear()
        print("»»—————————- INFINITE CLI RPG —————————-««")
        print("╔════════════════════════════════════════╗")
        print("║  ❮1❯  C O N T I N U E   G A M E  ❮1❯   ║")
        print("║    ❮2❯     N E W  G A M E      ❮2❯     ║")
        print("║    ❮3❯   H E L P   G U I D E   ❮3❯     ║")
        print("║    ❮0❯    E X I T   G A M E    ❮0❯     ║")
        print("╚════════════════════════════════════════╝")

        opt = validate_int_opt(int_input(), MAIN_MENU_OPTS)       
        
        if opt == 1:
            if not save_files:
                print("You don't have any game saved.")
                wait(4)
            else:
                print("SELECT")
                wait(5)
        elif opt == 2:
            print("NEW GAME")
            wait(4)

def select_save_menu(saves_data):
    clear()