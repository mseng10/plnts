import sys
from commands.create import Create
from commands.stats import Stats
from commands.need_water import NeedWaterCommand
from datetime import datetime

manaul_cmds = [Create(), Stats()]
auto_cmds = [NeedWaterCommand()]
i = " "


def print_help():
    print("Manual commands:")
    for cmd in manaul_cmds:
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
        for command in manaul_cmds:
            if key == command.key:
                command.process()
    else:
        for command in auto_cmds:
            if command.ready(datetime.now()):
                command.process()
print("GOODBYE")