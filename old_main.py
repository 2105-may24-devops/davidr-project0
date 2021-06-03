from blessed import Terminal
import random
import time
import menus

#   _____        __ _       _ _         _____                                     
#  |_   _|      / _(_)     (_) |       |  __ \                                    
#    | |  _ __ | |_ _ _ __  _| |_ ___  | |  | |_   _ _ __   __ _  ___  ___  _ __  
#    | | | '_ \|  _| | '_ \| | __/ _ \ | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \ 
#   _| |_| | | | | | | | | | | ||  __/ | |__| | |_| | | | | (_| |  __/ (_) | | | |
#  |_____|_| |_|_| |_|_| |_|_|\__\___| |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|
#                                                           __/ |                 
#                                                          |___/         

term = Terminal()

menu = [["Play"], ["Load"], ["Exit"]]


def display_main_menu(selection):
    term = Terminal()
    print(term.clear())
    print(term.home + term.clear + term.move_y(5) +
          term.green(term.center("Main Menu")))
    print(term.move_down(2))

    menu_string = "\t"

    for (idx, m) in enumerate(menu):

        # if idx == selection:
        #     print('{t.bold_green_reverse}{title}'.format(t=term, title=m[0]))
        # else:
        #     print('{t.normal}{title}'.format(t=term, title=m[0]))
        if idx == selection:
            menu_string += term.black_on_green(m[0]) + "\t"
        else:
            menu_string += term.green_on_black(m[0]) + "\t"

    print(term.center(menu_string))

# Play
# Basic game loops Overworld Explore > Point of Interest > Fight/Find item/money > Explore


def play():
    print(term.home + term.clear)
    player_alive = True
    distance = 0.0
    chance_of_encounter = .2

    while player_alive:
        print(term.home + term.clear)
        print(term.green(term.rjust(f"Distance: {round(distance, 2)}m")))

        # Determine if there's an encounter
        if random.random() <= chance_of_encounter:
            print(term.move_y(5) + term.black_on_green(term.center("Encounter!")))
            # If it's a point of interest open the explor submenu
            # Otherwise open the battle menu
        else:
            #// TODO: Add some random flavor text every once in a while
            
            print(term.move_y(5) + term.green(term.center("Regular exploring")))
        distance += .01
        time.sleep(1)


# Load
def load():
    pass

# Exit


def run_selection(selection):
    print(term.green_reverse('Running {}'.format(menu[selection][0])))
    if selection == 0:
        play()
    elif selection == 1:
        load()
    else:
        print(term.home + term.clear + term.move_down(10) +
              term.center("Thank you for playing"))
        print(term.home + term.move_y(term.height // 2))
        print(term.black_on_green(term.center('Press any key to exit.')))
        with term.cbreak(), term.hidden_cursor():
            term.inkey()
        exit()


# Title Screen

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


# Main Menu

with term.cbreak(), term.hidden_cursor():
    inp = term.inkey()

print(term.home + term.clear + term.move_y(5) +
      term.green(term.center("Main Menu")))
      
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

        selection = selection % len(menu)

        display_main_menu(selection)

    run_selection(selection)
