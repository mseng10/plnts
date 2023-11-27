# from cli.process import Process
# from models.plant import Plant
# from db import Session
# from util.util import Util
# from datetime import datetime
#
#
# class Archive(Process):
#     """Archive a plant command."""
#
#     def __init__(self) -> None:
#         Process.__init__(self, key="archive", description="Archive a plant.")
#
#     def process(self) -> None:
#         super().process()
#         db = Session()
#         filtered_plants: list[Plant] = db.query(Plant).all()
#         print("Current Geni (lol):")
#         for p in filtered_plants:
#             print(f"\t{p.genus}")
#         genus: str = self.input("Genus? ")
#         filtered_plants = [p for p in filtered_plants if p.genus == genus]
#
#         print("Current Types in Geni (lol):")
#         for p in filtered_plants:
#             print(f"\t{p.type}")
#         type: str = self.input("Type? ")
#         filtered_plants = [p for p in filtered_plants if p.type == type]
#
#         print("Current Names in Type:")
#         for p in filtered_plants:
#             print(f"\t{p.name}")
#         name: str = self.input("Name? ")
#         filtered_plants = [p for p in filtered_plants if p.name == name]
#
#         print("Which one?")
#         for p in filtered_plants:
#             print(f"\t{p.id}")
#         id: int = int(self.input("ID? ")) #TODO: Make better once we have multiple of same type
#         filtered_plants = [p for p in filtered_plants if p.id == id]
#
#         plant = filtered_plants[0]
#         print("--------------------")
#         print(f"{plant} to archive.")
#         while Util.confirm("Continue to update field on plant"):
#             plant.alive = False
#             plant.dead_on = datetime.now()
#             plant.cause = self.input("Cause of death? ")
#             db.commit()
#             print("Plant is is archived..")
#             print()
