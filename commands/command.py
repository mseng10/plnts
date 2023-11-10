from util.util import Util
from colorama import Fore

class Command:
    """Abstract Command class."""

    def __init__(self, key: str, description: str = "No description provided.") -> None:
        self.key: str = key
        self.description: str = description

    def __repr__(self):
        return f"{self.key} - {self.description}"

    def process(self) -> None:
        print("")
        print(f"Running {self.key} command")

    def input(self, question: str) -> any:
        while True:
            value = input(question)
            if value == "EXIT":
                print()
                print(Fore.RED + f"Attempting to exit {self.key} command.")
                if Util.confirm("Are you sure"):
                    raise Exception(f"Exiting {self.key} command.")
            # elif value == "OFF":
            #     print(Fore.RED + "Attempting to turn off the system.")
            #     if Util.confirm("Are you sure"):
            #         raise Exception("Exiting current command.")

