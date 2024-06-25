from utils.tools import singleton

@singleton
class FilePath(object):
    def __init__(self):
        self.path = None

    def changePath(self, new_path: str):
        '''Allows to change the save file path'''
        self.path = new_path

    def getPath(self) -> str:
        '''Returns the save file selected'''
        return self.path