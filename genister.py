import random, os
from os import system, name

def quit_program():
    clear_terminal()
    print("\n\t**Philasky Bot bids you farewell and a good day!**\n")
    ## Raises the "SystemExit" exception, exiting the program and executing clean-up handlers.
    ## This allows the exception to properly propagate up and cause the interpreter to exit. (Terminating all Python scripts)
    ## "sys.exit" uses "import sys" and rasies the "SystemExit" exception.
    raise SystemExit

def clear_terminal():
    ## Windows (os.name is 'nt)
    if name == 'nt':
        _ = system('cls')
    ## Linux & Mac (os.name is 'posix')
    else:
        _ = system('clear')

def __main__():
    clear_terminal()
    main_menu()

def main_menu():

    while(True):
        print("\n1. Generate Random Passphrase")
        print("2. Quit Program")

        main_input = input("\nGenister Command: ")

        if main_input == "1":
            generate_pass()
        elif main_input == "2":
            quit_program()

def copy_clipboard(text):
    #pbcopy = OSX - clip = Win - xclip = Linux
    #he strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def random_line(rand_line):
    #first using "open()" to open the text doc so that we can read from or write to it.
    #using "read()" to be able to read the doc contents.
    #splitline() method is used to split the lines at line boundaries. 
    #The function returns a list of lines in the string.
    lines = open(rand_line).read().splitlines()

    return random.choice(lines)

def generate_pass():
    clear_terminal()
    word1 = (random_line('genister_store.txt'))
    word2 = (random_line('genister_store.txt'))
    word3 = (random_line('genister_store.txt'))

    copy_clipboard(f"{word1} {word2} {word3}")
    #Return the length (the number of items) of an object. 
    #The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
    print("\nThe password character length is: ", len(f"{word1} {word2} {word3}"))
    print("\n************************************")
    print(f"   {word1} {word2} {word3}")
    print("************************************")

__main__()