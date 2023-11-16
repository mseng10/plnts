# from processes.command import Command
# from util.db_util import DBUtil
# from util.util import Util
# from models.plant import Plant
#
#
# class Water(Command):
#     """Water the plants that need to be watered command."""
#
#     def __init__(self):
#         Command.__init__(
#             self,
#             key="water",
#             description="Prompts the user to water the plants",
#         )
#
#     def process(self):
#         super().process(self)
#         DBUtil.update_plants(self.water_plants)
#
#     @staticmethod
#     def water_plants(plants: list[Plant]):
#         """Check for and water the provided plants."""
#         plants_need_water: list[Plant] = [p for p in plants if p.needs_water()]
#
#         if len(plants_need_water) == 0:
#             print("No plants need to be watered, yay.")
#             return
#
#         print("Plants that need water:")
#         for p in plants_need_water:
#             print(p)
#
#         if Util.confirm("All of them?"):
#             for p in plants:
#                 if p in plants_need_water:
#                     p.water()
#         elif Util.confirm("One by one?"):
#             for p in plants:
#                 if p in plants_need_water and Util.confirm(f"{p} water? "):
#                     p.water()
