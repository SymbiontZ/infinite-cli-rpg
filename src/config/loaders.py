from classes.config import Language, SaveFiles

def load_lang(config_data: dict[str, str]):
    if not "lang" in config_data:
        raise ValueError("There was an error and the language could not be found in your config.")
    
    lang = config_data.get("lang")

    config_lang = Language()
    
    config_lang.changeLang(lang)


def load_save_files(config_data: dict[str, int]):
    if not "last_save" in config_data:
        raise ValueError("There was an error and couldn't retrieve last save played in your config")
    
    last_save = config_data.get("last_save")

    save_files = SaveFiles()

    save_files.loadFiles()
    if save_files.hasAnyFile():
        save_files.updateLastSavePlayed(last_save)


