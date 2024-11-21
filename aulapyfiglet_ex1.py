import pyfiglet 
from colorama import Fore, Style , init , Back

text = "Ola, Mundo!"
ascii_art = pyfiglet.figlet_format(text, font='standard')
print(Fore.RED + ascii_art)
