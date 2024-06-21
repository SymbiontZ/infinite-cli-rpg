def new_savefile_dict (name:str, difficulty:int) -> dict:
    save_file = {
        "name": f"{name}",
        "difficulty": int(f"{difficulty}"),
        "level": 0,
        "stats": {
            "base": {
                "hp": 100,
                "atk": 25,
                "def":25,
            },
            "gained": {
                "hp": 0,
                "atk": 0,
                "def": 0,
            },
        },
        "items": [],
    }
    return save_file