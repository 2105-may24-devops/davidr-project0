from game_manager import Config
import json
import entity
import pathlib as Path
import jsonpickle
import os

player = entity.Player("bob", 5, 10, entity.Stats(2, 3, 4, 5))
config = Config()

def save(player, config):
    if not os.path.isfile("saves/"):
        os.mkdir("saves/")
    f = open("./saves/save1.json", "w")
    f.write(jsonpickle.encode([player, config], indent=4))
    f.close()
    

def load(filename):
    #open and read the file after the appending:
    if not os.path.isfile("saves/"):
        os.mkdir("saves/")
    if not os.path.isfile("saves/save1.json"): 
        raise FileNotFoundError
    f = open(filename, "r")
    
    return jsonpickle.decode(f.read())

#save(player, config)

# print(load("./saves/save1.json"))

# newPlayer = entity.Player("ronald", 132, 1, entity.Stats(22, 31, 43, 51))

# newPlayer = load("./saves/save1.json")[0]

# print(newPlayer.name)