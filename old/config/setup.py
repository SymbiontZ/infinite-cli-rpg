import os, json
from classes.config import SaveFiles, Language
from constants.paths import DATA_PATH, CONFIG_PATH, CONFIG_FILE_PATH, TRANSLATION_PATH
from config.loaders import load_lang, load_save_files
from utils.tools import wait

GLOBAL_CONFIG_DEFAULT: dict[str, str | int] = {
    "lang": "en",
    "last_save": -1,
}

def do_setup():
    try:
        if not os.path.exists(DATA_PATH):           
            os.mkdir(DATA_PATH)
        
        if not os.path.exists(TRANSLATION_PATH):
            raise FileNotFoundError("Can't run the game without translations files. Please, reinstall the package.")
        
        if not os.path.exists(CONFIG_PATH):
            os.mkdir(CONFIG_PATH)

        if not os.path.isfile(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH, "w") as config_file:
                config_file.write(json.dumps(GLOBAL_CONFIG_DEFAULT, indent= 4))

        with open(CONFIG_FILE_PATH, "r") as config_file:
            config_data = json.load(config_file)

        
        load_lang(config_data)
        load_save_files(config_data)
        Language().validateTranslations()
    
    except ValueError as e:
        print(e)
        
    except FileNotFoundError as e:
        print(e)
        exit(-1)


def save_config():  

    lang = Language().getLang()
    last_save = SaveFiles().last_save_played
    new_config_data = {
        "lang": f"{lang}",
        "last_save": last_save,
    }

    with open(CONFIG_FILE_PATH, "w") as config_file:
        config_file.write(json.dumps(new_config_data, indent=4))