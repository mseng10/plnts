import sys
from commands import Commands
i=" "
while True:
    i = sys.stdin.readline()
    if str(i).strip() == "quit":
        break
    elif str(i).strip() == "create":
        Commands.__create__()
    elif str(i).strip() == "water":
        Commands.__water__()
    elif str(i).strip() == "":
        continue
print("GOODBYE")