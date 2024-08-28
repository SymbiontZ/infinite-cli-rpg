import os, json
from constants.paths import DATA_PATH, TRANSLATION_PATH
from utils.tools import singleton
@singleton
class SaveFilePath(object):
    def __init__(self):
        self.path = None

    def changePath(self, new_path: str):
        '''Allows to change the save file path'''
        self.path = new_path

    def getPath(self) -> str:
        '''Returns the save file selected'''
        return self.path
    
@singleton
class Language(object):
    '''
    Singleton class to manage language settings and translations
    '''
    def __init__(self):
        self.lang: str = "en"
        self.supported_langs: list[str] = ["en", "es"]
    
    def changeLang(self, new_lang: str) -> bool:
        '''
        Changes the language which messages will appear.
        '''
        if new_lang in self.supported_langs:
            self.lang = new_lang
            return True
        return False
        

    def getLang(self) -> str:
        '''
        Returns the actual language used on game.
        '''
        return self.lang
    
    def getLangTranslations(self) -> dict[str,str]:

        with open(self.getTranslationFilePath(self.lang), "r") as lang_file:
            return json.loads(lang_file)
    
    def validateTranslations(self):
        #os.path.split(lang)[0]: selects [name] from name.ext. Example: en.json -> en
        #os.listsdir(TRANSLATION_PATH): List of translations files. Example: ["en.json", "es.json", ...]
        
        available_langs = [os.path.splitext(lang)[0] for lang in os.listdir(TRANSLATION_PATH)]

        return set(available_langs) == set(self.supported_langs)
    
    def validateLang(self):
        if self.lang not in self.supported_langs:
            self.lang = "en"
    
    @staticmethod
    def getTranslationFilePath(lang:str) -> str:
        try:
            TRANSLATION_FILE_PATH = os.path.join(TRANSLATION_PATH, lang)
            if not os.path.exists(TRANSLATION_FILE_PATH):
                raise FileNotFoundError("Translation File for language selected was not found")
            
            return TRANSLATION_FILE_PATH
        
        except FileNotFoundError as e:
            print(e)
            exit(-1)

@singleton
class SaveFiles(object):
    '''
    Singleton class for managing and loading save files from a directory.

    Attributes:
    -----------
    files : dict[int, str]
        A dictionary where keys are file indexes and values file names.

    Methods:
    --------
    has_files() -> bool:
        Checks if any file has been loaded into 'files' dictionary.
    '''
    def __init__(self):
        self.files: dict[int, str] = {}
        self.last_save_played: int = -1

    def hasAnyFile(self) -> bool:
        return bool(self.files)
    
    def loadFiles(self):

        file_list = os.listdir(DATA_PATH)
        file_list = self.removeNotJSONFiles(file_list)

        for index, element in enumerate(file_list, start=1):
            self.files[index] = element
    
    def createFile(self):
        slot = str(len(self.files))

    def updateLastSavePlayed(self, id: int):
        if id in self.files:
            self.last_save_played = id

    @staticmethod
    def removeNotJSONFiles(file_list: list[str]) -> list[str]:
        '''
        Remove directories and files that not ends with .json, in order to get only save files.
        '''
        return [file for file in file_list if file.endswith(".json")]
    