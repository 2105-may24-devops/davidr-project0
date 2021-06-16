import sys
import menus
import sys
from blessed import Terminal

#   _____        __ _       _ _         _____                                     
#  |_   _|      / _(_)     (_) |       |  __ \                                    
#    | |  _ __ | |_ _ _ __  _| |_ ___  | |  | |_   _ _ __   __ _  ___  ___  _ __  
#    | | | '_ \|  _| | '_ \| | __/ _ \ | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \ 
#   _| |_| | | | | | | | | | | ||  __/ | |__| | |_| | | | | (_| |  __/ (_) | | | |
#  |_____|_| |_|_| |_|_| |_|_|\__\___| |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|
#                                                           __/ |                 
#                                                          |___/                  

term = Terminal()

# non-interactive mode
if len(sys.argv) > 1:
  # print("Assuming direct control")
  from entity import Player, Entity
  from game_manager import Config
  from fileio import save
  import random

  random.seed(1337)
  player = Player(health=100)
  enemy = Entity(health=100)

  if sys.argv[1].lower() == "attack":
    player.stats.evasion = enemy.stats.evasion = 0
    player.stats.attack = int(sys.argv[2])
    enemy.stats.attack = int(sys.argv[3])
    player.attack(enemy)
    enemy.attack(player)
  
  elif sys.argv[1].lower() == "guard":
    player.stats.evasion = enemy.stats.evasion = 0
    player.stats.attack = int(sys.argv[2])
    enemy.stats.attack = int(sys.argv[3])
    player.stats.defense = int(sys.argv[4])
    enemy.stats.defense = int(sys.argv[5])
    player.guard()
    enemy.attack(player)
    enemy.guard()
    player.attack(enemy)

  elif sys.argv[1].lower() == "save":
    if sys.argv[2].lower() == "player":
      player = Player(sys.argv[3], int(sys.argv[4]), int(sys.argv[5]))
      config = Config()
      save(player, config, "PLAYERTEST")
    elif sys.argv[2].lower() == "config":
      player = Player()
      config = Config(sys.argv[3].split(), float(sys.argv[4]))
      save(player, config, "CONFIGTEST")
    else:
      print("Unsupported command.")

  elif sys.argv[1].lower() == "load":
    if sys.argv[2].lower() == "player":
      player = Player()
      config = Config()
      save(player, config, "PLAYERTEST")
    elif sys.argv[2].lower() == "config":
      player = Player()
      config = Config(sys.argv[3].split(), float(sys.argv[4]))
      save(player, config, "CONFIGTEST")
    else:
      print("Unsupported command.")
  
  else:
    print("Unsupported command.")
    exit(1)

# interactive mode
else:

  print(term.home + term.clear + term.move_y(term.height // 2 - 10))
  lines = term.wrap("""    _____        __ _       _ _         _____                                     
  |_   _|      / _(_)     (_) |       |  __ \                                   
    | |  _ __ | |_ _ _ __  _| |_ ___  | |  | |_   _ _ __   __ _  ___  ___  _ __ 
    | | | '_ \|  _| | '_ \| | __/ _ \ | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \\
    _| |_| | | | | | | | | | | ||  __/ | |__| | |_| | | | | (_| |  __/ (_) | | | |
   |_____|_| |_|_| |_|_| |_|_|\__\___| |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|
                                                            __/ |                
                                                          |___/                 """, width=82, drop_whitespace=False, replace_whitespace=False)

  for line in lines:
      print(term.green_on_black(term.center(line)))

  print(term.home + term.move_y(term.height // 2))
  print(term.black_on_green(term.center('Press any key to continue.')))

  with term.cbreak(), term.hidden_cursor():
      term.inkey()


  # Main Menu
  menus.main_menu_loop()
