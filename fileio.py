from game_manager import Config
import entity
import jsonpickle
import os

player = entity.Player("bob", 5, 10, entity.Stats(2, 3, 4, 5))
config = Config()

def save(player, config):
    if not os.path.isdir("saves/"):
        os.makedirs("saves/", exist_ok=True)
    f = open("./saves/save1.json", "w")
    f.write(jsonpickle.encode([player, config], indent=4))
    f.close()
    

def load(filename):
    #open and read the file after the appending:
    if not os.path.isdir("saves/"):
        os.makedirs("saves/", exist_ok=True)
    if not os.path.isfile("saves/save1.json"): 
        raise FileNotFoundError
    f = open(filename, "r")
    
    return jsonpickle.decode(f.read())