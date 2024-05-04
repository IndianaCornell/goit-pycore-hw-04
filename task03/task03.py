import sys
from pathlib import Path
from colorama import Fore, Style

try:
    path = Path(sys.argv[1])
    print(Fore.RED + path.name + "/")
except IndexError:
    print("Невірка кількість аргументів.")
    sys.exit()

primal_indent = len(path.parts)

def parse_file(path):
    try:
        for el in path.iterdir():
            indent = "\t" * (len(el.parts) - primal_indent) 
            if el.is_dir():
                dir_indent =  "\t" * (len(el.parts) - primal_indent)
                print(Fore.RED + f"\v {dir_indent} {el.name}/")
                parse_file(el)
            else:
                print(Fore.BLUE + f" {indent} {el.name}" ,sep='\n')
                print(Style.RESET_ALL)

    except FileNotFoundError:
        print("Вказаної директорії не існує.")
    except NotADirectoryError:
        print("Ви вказуєте шлях до файлу, але не директорії.")

parse_file(path)