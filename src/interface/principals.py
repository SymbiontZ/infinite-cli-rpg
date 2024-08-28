from utils.tools import clear,int_input, wait
from utils.validators import validate_int_opt
from classes.config import SaveFiles, Language

from interface.exceptions import exceptions_msg

MAIN_MENU_OPTS = [0,1,2,3,4,5]

def main_menu():
    opt = None
    while opt is None or opt != 0:
        save_files = SaveFiles()
        lang = Language()
        clear()
        print("»»—————————- INFINITE CLI RPG —————————-««")
            

        opt = validate_int_opt(int_input(), MAIN_MENU_OPTS)

        if opt == 1:
            if save_files.last_save_played != -1:
                print("cargar partida")
            else:
                print(exceptions_msg("nolastsave"))
                input()

        elif opt == 2:
            select_save_menu(save_files)


def select_save_menu(save_files: SaveFiles):
    for k, v in save_files.files:
        print("I")