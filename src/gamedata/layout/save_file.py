def new_savefile_dict (name:str, difficulty:int) -> dict:
    save_file = {
        "name": {name},
        "difficulty": {difficulty},
        "level": 0,
        "stats": {
            "base": {
                "hp": 100,
                "atk": 25,
                "def":25,
            },
            "gained": {
                "hp"
                
            }
        },
    }
    return save_file