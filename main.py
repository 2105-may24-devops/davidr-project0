from menus.menus import main_menu_loop
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

main_menu_loop()