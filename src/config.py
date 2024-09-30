import os
from pathlib import Path

LocalPath: Path = os.getcwd()
DBPath: Path = os.path.join(LocalPath, "gamedata.db")