import os

LOCAL_PATH = os.getcwd()

DATA_PATH = os.path.join(LOCAL_PATH,"data")

CONFIG_PATH = os.path.join(DATA_PATH, "config")

CONFIG_FILE_PATH = os.path.join(CONFIG_PATH, "global_config.json")

TRANSLATION_PATH = os.path.join(LOCAL_PATH, "src", "translations")