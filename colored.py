$ pip install colorama
# colorama_demo.py
from colorama import init, Fore, Back, Style

# Initializes Colorama
init(autoreset=True)

print(Style.BRIGHT + Back.YELLOW + Fore.RED + "CHEESY")
