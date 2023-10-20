import sys
from commands.create import Create

manual_commands = [
    Create("create")
]
auto_commands = [

]
i=" "
while True:
    i = sys.stdin.readline()
    key = str(i).strip()
    if key == "quit":
        break
    elif len(key) > 0:
        for command in manual_commands:
            print(key)
            if key == command.key:
                command.process()
    else:
        for command in auto_commands:
            command.process()
print("GOODBYE")