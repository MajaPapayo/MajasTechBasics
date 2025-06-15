import random
import cowsay
import pyjokes
from colorama import Fore, Style, init


init()

colors = [Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.GREEN, Fore.MAGENTA, Fore.CYAN]
randomcolor = random.choice (colors)
joke = pyjokes.get_joke()
print( randomcolor + "funny code-cow incoming :\n")
cowsay.cow(joke)
print(Style.RESET_ALL)

