import sys
from commands.plant_cmds.create import Create
from commands.stats import Stats
from commands.plant_cmds.water import Water
from commands.plant_cmds.need_water import NeedWaterCommand
from datetime import datetime

manual_cmds = [Create(), Stats(), Water()]
auto_cmds = [NeedWaterCommand()]
i = " "


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
print("GOODBYE")
