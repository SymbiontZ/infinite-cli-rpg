import os, json, jsonschema
from typing import Union, Optional  
from jsonschema import validate
import jsonschema.exceptions
from constants.datascheme import DATA_SCHEME
from constants.paths import DATA_PATH

def validate_games(save_files: list[str]) -> bool:
    '''
    This function verify if all the save files are OK, given by a list.\n
    Returns True if all save files are correct, if not returns False.
    '''

    for filename in save_files:
        file_dir = os.path.join(DATA_PATH, filename)
        try:
            if not os.path.isfile(file_dir):
                raise ValueError(f"El archivo {filename} no existe.")
            
            with open(file_dir) as file:
                data = json.load(file)

            validate(instance=data, schema=DATA_SCHEME)
            
            return True

        except ValueError as e:
            print(e)
            return False
        except OSError as e:
            print(e)
            return False
        
        except jsonschema.ValidationError as e:
            print(f"The file {filename} is corrupted")
            return False
        

def validate_int_opt(opt: int, opt_select:Union[list[int], dict[int, str]]) -> Optional[Union[int, tuple[int, str]]]:
    if isinstance(opt_select, list):
        if opt in opt_select:
            return opt
        return None
    elif isinstance(opt_select, dict):
        if opt in opt_select:
            return (opt, opt_select[opt])
        return None
    return None