from fileio import load, save
from game_manager import *
from blessed import Terminal

term = Terminal()

# MAIN MENU 

main_menu = ["Play", "Load", "Exit"]

def display_main_menu(selection):
    
    print(term.clear())
    print(term.home + term.clear + term.move_y(5) +
          term.green(term.center("Main Menu")))
    print(term.move_down(2))

    menu_string = "    "

    for (idx, m) in enumerate(main_menu):
        if idx == selection:
            menu_string += term.black_on_green(m) + "    "
        else:
            menu_string += term.green_on_black(m) + "    "

    print(term.center(menu_string))

def run_main_menu_selection(selection):
    print(term.green_reverse('Running {}'.format(main_menu[selection][0])))
    if selection == 0:
        play()
    elif selection == 1:
        load("./saves/save1.json")
        play()
    else:
        print(term.home + term.clear + term.move_down(10) +
                term.center("Thank you for playing"))
        print(term.home + term.move_y(term.height // 2))
        print(term.black_on_green(term.center('Press any key to exit.')))
        with term.cbreak(), term.hidden_cursor():
            term.inkey()
        exit()

def main_menu_loop(): 
    selection = 0
    display_main_menu(selection)
   
    selection_inprogress = True
    with term.cbreak():
        while selection_inprogress:
            key = term.inkey()
            if key.is_sequence:
                if key.name == 'KEY_TAB':
                    selection += 1
                if key.name == 'KEY_RIGHT':
                    selection += 1
                if key.name == 'KEY_LEFT':
                    selection -= 1
                if key.name == 'KEY_ENTER':
                    selection_inprogress = False
            elif key:
                print("got {0}.".format(key))

            selection = selection % len(main_menu)

            display_main_menu(selection)

        run_main_menu_selection(selection)

# INVESTIGATION MENU

investigation_menu = ["Investiagte", "Leave"]

def display_investiation_menu(selection):
    
    print(term.clear())
    print(term.home + term.clear + term.move_y(5) +
          term.green(term.center("Investigation Menu")))
    print(term.move_down(2))

    menu_string = "    "

    for (idx, m) in enumerate(investigation_menu):
        if idx == selection:
            menu_string += term.black_on_green(m) + "    "
        else:
            menu_string += term.green_on_black(m) + "    "

    print(term.center(menu_string))

def run_investigation_selection(selection):
    # Investigate option
    if selection == 0:
        #// TODO: Decide what you can find
        print(term.home + term.move_y(term.height // 2))        
        print(term.black_on_green(term.center('You find nothing interesting')))
        with term.cbreak(), term.hidden_cursor():
            term.inkey()
    # Leave option
    elif selection == 1:
        #// TODO: Maybe something interesting can happen here?
        print(term.home + term.move_y(term.height // 2))
        print(term.black_on_green(term.center('You decide to leave')))
        with term.cbreak(), term.hidden_cursor():
            term.inkey()

def investigation_menu_loop(): 
    selection = 0
    display_investiation_menu(selection)
   
    selection_inprogress = True
    with term.cbreak():
        while selection_inprogress:
            key = term.inkey()
            if key.is_sequence:
                if key.name == 'KEY_TAB':
                    selection += 1
                if key.name == 'KEY_RIGHT':
                    selection += 1
                if key.name == 'KEY_LEFT':
                    selection -= 1
                if key.name == 'KEY_ENTER':
                    selection_inprogress = False
            elif key:
                print("got {0}.".format(key))

            selection = selection % len(investigation_menu)

            display_investiation_menu(selection)

        run_investigation_selection(selection)

# FIGHT MENU

fight_menu = ["Fight", "Guard", "Use Item", "Flee"]

def display_fight_menu(selection, player, enemy, clear = True):
    
    if clear: print(term.clear())
    print(term.home + term.ljust(f"{player.name} HP: {player.health}"))
    print(term.rjust(f"{enemy.name} HP: {enemy.health}"))
    print(term.home + term.move_y(5) + term.green(term.center("Fight Menu")))
    print(term.move_down(2))

    menu_string = "    "

    for (idx, m) in enumerate(fight_menu):
        if idx == selection:
            menu_string += term.black_on_green(m) + "    "
        else:
            menu_string += term.green_on_black(m) + "    "

    print(term.center(menu_string) + term.move_down(2))

def run_fight_menu_selection(selection, player, enemy, escaped):
    # Fight
    if selection == 0:
        #// TODO: Decide what you can find
        print(term.home + term.move_y(term.height // 2))        
        #print(term.black_on_green(term.center('You strike the enemy')))
        player.attack(enemy)
        with term.cbreak(), term.hidden_cursor():
            term.inkey()
    # Guard
    elif selection == 1:
        #// TODO: Maybe something interesting can happen here?
        print(term.home + term.move_y(term.height // 2))
        #print(term.black_on_green(term.center('You brace yourself for an attack')))
        player.guard()
        with term.cbreak(), term.hidden_cursor():
            term.inkey()
    # Use Item - probably gonna get removed
    elif selection == 2:
        #// TODO: Maybe something interesting can happen here?
        print(term.home + term.move_y(term.height // 2))
        print(term.black_on_green(term.center('You used an item')))
        with term.cbreak(), term.hidden_cursor():
            term.inkey()
    # Flee
    elif selection == 3:
        #// TODO: Maybe something interesting can happen here?
        escaped[0] = player.flee(enemy)
        print(term.home + term.move_y(term.height // 2))
        if escaped[0]:
            print(term.black_on_green(term.center(f'{player.name} has fled the battle')))
        else:
            print(term.black_on_green(term.center(f'{player.name} failed to flee')))
        with term.cbreak(), term.hidden_cursor():
            term.inkey()

def fight_menu_loop(player, enemy, escaped, clear = False):
    selection = 0
    display_fight_menu(selection, player, enemy, clear)
   
    selection_inprogress = True
    with term.cbreak():
        while selection_inprogress:
            key = term.inkey()
            if key.is_sequence:
                if key.name == 'KEY_TAB':
                    selection += 1
                if key.name == 'KEY_RIGHT':
                    selection += 1
                if key.name == 'KEY_LEFT':
                    selection -= 1
                if key.name == 'KEY_ENTER':
                    selection_inprogress = False
            elif key:
                print("got {0}.".format(key))

            selection = selection % len(fight_menu)

            display_fight_menu(selection, player, enemy, clear)

        run_fight_menu_selection(selection, player, enemy, escaped)

# IDLE MENU

idle_menu = ["Continue Forward", "Save", "Load", "Exit"]

def display_idle_menu(selection, player, config):
    
    print(term.clear())
    print(term.home + term.ljust(f"{player.name} HP: {player.health}"))
    print(term.rjust(f"Distance traveled: {round(config.distance, 2)}m"))
    print(term.home + term.move_y(5) +
          term.green(term.center("Idle Menu")))
    print(term.move_down(2))

    menu_string = "    "

    for (idx, m) in enumerate(idle_menu):
        if idx == selection:
            menu_string += term.black_on_green(m) + "    "
        else:
            menu_string += term.green_on_black(m) + "    "

    print(term.center(menu_string))

def run_idle_menu_selection(selection, player, config):
    # Continue forward
    if selection == 0:
        pass
    # Save
    elif selection == 1:
        save(player, config)
        print(term.home + term.move_y(term.height // 2))        
        print(term.black_on_green(term.center('Saved to saves/save1.json')))

        with term.cbreak(), term.hidden_cursor():
            term.inkey()
    # Load
    elif selection == 2:
        loaded = load("./saves/save1.json")
        player.load(loaded[0])
        config.load(loaded[1])

        print(term.home + term.move_y(term.height // 2))        
        print(term.black_on_green(term.center('Loaded from saves/save1.json')))

        with term.cbreak(), term.hidden_cursor():
            term.inkey()
    else:
        print(term.home + term.clear + term.move_down(10) +
                term.center("Thank you for playing"))
        print(term.home + term.move_y(term.height // 2))
        print(term.black_on_green(term.center('Press any key to exit.')))
        with term.cbreak(), term.hidden_cursor():
            term.inkey()
        exit()

def idle_menu_loop(player, config): 
    selection = 0
    display_idle_menu(selection, player, config)
   
    selection_inprogress = True
    with term.cbreak():
        while selection_inprogress:
            key = term.inkey()
            if key.is_sequence:
                if key.name == 'KEY_TAB':
                    selection += 1
                if key.name == 'KEY_RIGHT':
                    selection += 1
                if key.name == 'KEY_LEFT':
                    selection -= 1
                if key.name == 'KEY_ENTER':
                    selection_inprogress = False
            elif key:
                print("got {0}.".format(key))

            selection = selection % len(idle_menu)

            display_idle_menu(selection, player, config)

        run_idle_menu_selection(selection, player, config)