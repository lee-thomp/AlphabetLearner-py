#!/usr/bin/python3

import signal
import sys
import random

# An interactive test program to learn the position of letters in the alphabet

# Track correct/false
correct_count   = 0
false_count     = 0

# Handle Ctrl-C to exit program
def signal_handler(signal, frame):
    print(); print();
    print(f"Correct/False:\t{correct_count}/{false_count}")
    sys.exit(0)

# Attach exit handler
signal.signal(signal.SIGINT, signal_handler)


# Main function
def main ():

    # Pull in score counters as global
    global correct_count
    global false_count
    
    # Escape codes for bold and non-bold
    BOLD    = '\033[1m'
    RESET   = '\033[m'
    GREEN   = '\033[32m'

    # Ordinal indicator suffixes
    indicator = ('', 'st', 'nd', 'rd') + ('th',)*17 + ('st', 'nd', 'rd') + ('th',)*3

    print('''
    === Interactive Alphabet Game ===
        use Ctrl-C to exit
        ''')

    while True:

        # Create random letter-position pair
        position    = random.randrange(1, 26)
        letter      = chr(ord('a') + position - 1)

        # Flip a coin on whether to ask for letter or position
        if (random.choice([True, False])):
            answer = input(f"{BOLD}Position of '{letter}':\t{RESET}")
        else:
            answer = input(f"{BOLD}The {position}{indicator[position]} letter:\t{RESET}")

        # Repeat back if answer was correct or not
        if answer in [str(position), letter]:
            print(f"{BOLD}{GREEN}Correct{RESET}, '{letter}' is {position}{indicator[position]} in the alphabet")
            correct_count += 1
        else:
            print(f"False, '{letter}' is {position}{indicator[position]} in the alphabet")
            false_count += 1

        # Empty line
        print()

# Call main
if __name__ == "__main__":
    main()
