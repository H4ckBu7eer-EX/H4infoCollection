from colorama import Fore

def hprint(context='',  # 内容。
           tf=True,  # 是否在内容前面带"[*]"
           enter=True,  # 是否在内容之后回车
           logo=False
           ):
    if tf:
        if enter:
            print(f'[*]{context}')
        else:
            print(f'[*]{context}', end='')
    else:
        if enter:
            print(f'{context}')
        else:
            print(f'{context}', end='')

def print_red(context, tf=True):
    hprint(Fore.RED + context + Fore.RESET, tf=tf)


def print_green(context, tf=True):
    hprint(Fore.GREEN + context + Fore.RESET, tf=tf)


def print_white(context, tf=True):
    hprint(Fore.WHITE + context + Fore.RESET, tf=tf)


def print_black(context, tf=True):
    hprint(Fore.BLACK + context + Fore.RESET, tf=tf)


def print_yellow(context, tf=True):
    hprint(Fore.YELLOW + context + Fore.RESET, tf=tf)


def print_blue(context, tf=True):
    hprint(Fore.BLUE + context + Fore.RESET, tf=tf)