from classes.config import Language

nolastsave = {
        "en": "<<< No valid last saved game. Press [enter] to continue... >>>",
        "es": "<<< No hay partidas guardadas. Press [enter] to continue... >>>"
    }


def exceptions_msg(index: str, lang: str = None):
    except_dict = {
        "nolastsave": nolastsave,
    }

    if not lang:
        lang = Language().getLang()
    
    message_dict = except_dict.get(index)

    if message_dict:
        return message_dict.get(lang, message_dict["en"])
    else:
        return f"<<<No valid exception message for '{index}'>>>"


    