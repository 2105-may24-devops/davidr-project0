from entity import Entity, Player, Stats
import random
import time
import menus.menus

from blessed import Terminal

class Config():
    def __init__(self, enemy_names = ["Rat", "Thug", "Pirate"], distance = 0.0, chance_of_encounter = .1, chance_of_battle = .9, walking_speed = .1):
        self.enemy_names = enemy_names
        self.distance = distance
        self.chance_of_encounter =  chance_of_encounter
        self.chance_of_battle = chance_of_battle
        self.walking_speed = walking_speed
    
    def load(self, config):
        self.enemy_names = config.enemy_names
        self.distance = config.distance
        self.chance_of_encounter =  config.chance_of_encounter
        self.chance_of_battle = config.chance_of_battle
        self.walking_speed = config.walking_speed

def play():
    term = Terminal()
    print(term.home + term.clear)
    config = Config()
    player = Player("Protag", 10, 10, Stats(2, 4, 3, 4))


    while player.health > 0:
        print(term.home + term.clear)
        print(term.green(term.rjust(f"Distance: {round(config.distance, 2)}m")))

        # Determine if there's an encounter
        if random.random() <= config.chance_of_encounter:
            print(term.move_y(5) + term.black_on_green(term.center("!DANGER!")))
            # If there's a point of interest open the explore submenu
            # Otherwise open the battle menu
            if random.random() >= config.chance_of_battle:
                menus.menus.investigation_menu_loop()
            else:
                enemy = Entity(config.enemy_names[random.randrange(0, len(config.enemy_names))], player.level + random.randrange(-1, 1), 5, Stats(2, 2, 2, 2))
                print(term.home + term.move_y(term.height // 2))
                print(term.black_on_green(term.center(f'{enemy.name} is preparing to fight you.')))
                with term.cbreak(), term.hidden_cursor():
                    term.inkey()
                
                escaped = [False]
                # Make sure everyone is alive or the player hasn't escaped before starting a new turn
                while player.health > 0 and enemy.health > 0 and not escaped[0]:
                    print(f"{player.name} HP: {player.health} | {enemy.name} HP: {enemy.health}")
                    # Reset player guard
                    player.is_guarding = False

                    # Player's turn
                    menus.menus.fight_menu_loop(player, enemy, escaped, True)
                    
                    # Reset enemy guard
                    enemy.is_guarding = False
                    # Enemy's turn - Only do this if they're still alive and player hasn't escaped
                    if enemy.health > 0 and not escaped[0]:
                        # 50% chance the enemy will attack or guard
                        if (random.random() >= .5):                            
                            enemy.guard()
                        else:
                            enemy.attack(player)
                        with term.cbreak(), term.hidden_cursor():
                                term.inkey()

                if enemy.health <= 0:            
                    print(f"{enemy.name} has been defeated.")
                if player.health <= 0:            
                    print(f"{player.name} has been defeated.")
        else:
            #// TODO: Add some random flavor text every once in a while
            
            print(term.move_y(5) + term.green(term.center("Regular exploring")))
            menus.menus.idle_menu_loop(player, config)
            
            

        config.distance += config.walking_speed
        time.sleep(1)

    # GAME OVER
    print(term.home + term.clear + term.move_down(10) + term.center("Game Over!"))
    print(term.home + term.move_y(term.height // 2))
    print(term.black_on_green(term.center('Press any key to exit.')))
    with term.cbreak(), term.hidden_cursor():
        term.inkey()

# def load():
#     pass