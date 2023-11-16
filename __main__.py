import sys
from processes.manual.create import Create
from processes.manual.stats import Stats

from processes.manual.water import Water
# from processes.manual.update import Update
from processes.recurrent.check_water import CheckWater
from models.config import Config
from datetime import datetime
from colorama import init, Fore


def run() -> None:
    # manual_processes = [Create(), Stats(), Water(), Update()]
    manual_processes = [Create(), Stats(), Water()]
    auto_processes = [CheckWater()]

    def print_help():
        print("----------------")
        print(Fore.LIGHTBLUE_EX + "Manual processes:")
        for cmd in manual_processes:
            print(cmd)
        print("----------------")
        print(Fore.LIGHTBLUE_EX + "Auto processes:")
        for cmd in auto_processes:
            print(cmd)
        print("----------------")

    while True:
        i = sys.stdin.readline()
        key = str(i).strip()
        if key == "quit" or key == "exit":
            break
        elif key == "help":
            print_help()
        elif len(key) > 0:
            for process in manual_processes:
                if key == process.key:
                    try:
                        process.process()
                    except Exception as e:
                        print(f"{e}\n")
            for process in auto_processes:
                if key == process.key:
                    try:
                        process.process()
                    except Exception as e:
                        print(f"{e}\n")
        else:
            for process in auto_processes:
                if process.ready(datetime.now()):
                    process.process()
    print(Fore.GREEN + "GOODBYE:)")


if __name__ == "__main__":
    init(autoreset=True)
    test_mode = True if len(sys.argv) == 2 and sys.argv[1] == "--test" else False
    config = Config(test_mode=test_mode)
    print(Fore.LIGHTBLUE_EX + f"{config}\n")
    run()
