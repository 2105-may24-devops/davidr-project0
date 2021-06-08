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
  import random

  random.seed(1337)
  player = Player()
  enemy = Entity()

  if sys.argv[1].lower() == "attack":
    player.attack(enemy)
    enemy.attack(player)
  
  if sys.argv[1].lower() == "guard":
    player.guard()
    enemy.attack(player)
    enemy.guard()
    player.attack(enemy)

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
