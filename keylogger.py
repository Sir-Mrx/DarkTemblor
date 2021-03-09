import sys
import os,time


def banner():
    os.system("cls" or "clear")
    print(+"""\n
  


    ██████   █████  ██████  ██   ██ ████████ ███████ ███    ███ ██████  ██       ██████  ██████  
    ██   ██ ██   ██ ██   ██ ██  ██     ██    ██      ████  ████ ██   ██ ██      ██    ██ ██   ██ 
    ██   ██ ███████ ██████  █████      ██    █████   ██ ████ ██ ██████  ██      ██    ██ ██████  
    ██   ██ ██   ██ ██   ██ ██  ██     ██    ██      ██  ██  ██ ██   ██ ██      ██    ██ ██   ██ 
    ██████  ██   ██ ██   ██ ██   ██    ██    ███████ ██      ██ ██████  ███████  ██████  ██   ██ 
                                                                                                 
    ##############################################################################################
    ##                           Cod                                                               ##
    ##                                                                                          ##
    ##                                                                                          ##
    ##                                                                                          ##
    ##                                                                                          ##
    ##############################################################################################
    
    
    
    
    
    
    
    
    
    """)

try :
    from colorama import Fore,init
    init()
except :
        os.system("cls" or "clear")
        print(Fore.RED+"""\n Please Install colorama in CMD ==> pip install colorama
        """)

#---------------------------------------------------------------------------------------

try :
    from pynput import keyboard,mouse
except :

    os.system("cls" or "clear")
    print(Fore.RED+"""\n Please Install pynput in CMD ==> pip install pynput
    """)

#----------------------------------------------------------------------------------------








def on_click(x, y, button, pressed):
    print(f"{x} : {y} : {button} - {pressed}")

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))



def mouse_log():
    with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as lst:
    lst.join()
mouse_log()