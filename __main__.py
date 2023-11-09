import sys
from commands.plant_cmds.create import Create
from commands.stats import Stats
from commands.plant_cmds.water import Water
from commands.plant_cmds.update import Update
from commands.plant_cmds.need_water import NeedWaterCommand
from models.config import Config
from datetime import datetime
from colorama import init, Fore

def run() -> None:
    manual_cmds = [Create(), Stats(), Water(), Update()]
    auto_cmds = [NeedWaterCommand()]

    def print_help():
        print("Manual commands:")
        for cmd in manual_cmds:
            print(cmd)
        print("----------------")
        print("Auto commands:")
        for cmd in auto_cmds:
            print(cmd)

    while True:
        i = sys.stdin.readline()
        key = str(i).strip()
        if key == "quit" or key == "exit":
            break
        elif key == "help":
            print_help()
        elif len(key) > 0:
            for command in manual_cmds:
                if key == command.key:
                    command.process()
        else:
            for command in auto_cmds:
                if command.ready(datetime.now()):
                    command.process()
    print(Fore.GREEN + "GOODBYE:)")


if __name__ == "__main__":
    init(autoreset=True)
    test_mode = True if len(sys.argv) == 2 and sys.argv[1] == "--test" else False
    config = Config(test_mode=test_mode)
    print(Fore.LIGHTBLUE_EX + f'{config}')
    print()
    run()
