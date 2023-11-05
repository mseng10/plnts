import sys
from commands.create import Create
from commands.stats import Stats
from commands.need_water import NeedWaterCommand
from datetime import datetime

manual_commands = [Create("create"), Stats("stats")]
auto_commands = [NeedWaterCommand()]
i = " "
while True:
    i = sys.stdin.readline()
    key = str(i).strip()
    if key == "quit" or key == "exit":
        break
    elif len(key) > 0:
        for command in manual_commands:
            if key == command.key:
                command.process()
    else:
        for command in auto_commands:
            if command.ready(datetime.now()):
                command.process()
print("GOODBYE")
