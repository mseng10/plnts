# from util.util import Util
# from colorama import Fore
#
#
# class Process:
#     """Abstract Command class."""
#
#     def __init__(self, key: str, description: str = "No description provided.") -> None:
#         self.key: str = key
#         self.description: str = description
#
#     def __repr__(self):
#         return f"{self.key} - {self.description}"
#
#     def process(self) -> None:
#         print(f"\nRunning {self.key} command")
#
#     def input(self, question: str) -> any:
#         while True:
#             value = input(question)
#             if value == "CANCEL":
#                 print()
#                 print(Fore.RED + f"Attempting to exit {self.key} command.")
#                 if Util.confirm("Are you sure"):
#                     raise Exception(f"Exiting {self.key} command.")
#             elif value == "EXIT":
#                 print(Fore.RED + f"Attempting to exit program {self.key}.")
#                 if Util.confirm("Are you sure"):
#                     Util.system_exit()
#             else:
#                 return value
