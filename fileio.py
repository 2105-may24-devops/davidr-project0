from game_manager import Config
import entity
import jsonpickle
import os

player = entity.Player("bob", 5, 10, entity.Stats(2, 3, 4, 5))
config = Config()

def save(player, config, slot = 1):
    if not os.path.isdir("saves/"):
        os.makedirs("saves/", exist_ok=True)
    f = open(f"./saves/save{slot}.json", "w")
    f.write(jsonpickle.encode([player, config], indent=4))
    f.close()
    

def load(slot = 1):
    #open and read the file after the appending:
    if not os.path.isdir("saves/"):
        os.makedirs("saves/", exist_ok=True)
    if not os.path.isfile(f"saves/save{slot}.json"): 
        raise FileNotFoundError
    f = open(f"saves/save{slot}.json", "r")
    
    return jsonpickle.decode(f.read())