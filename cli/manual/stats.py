# from cli.process import Process
#
# from db import Session
# from models.plant import Plant
#
#
# class Stats(Process):
#     """Calculate and display plant data set stats command."""
#
#     def __init__(self):
#         Process.__init__(
#             self,
#             key="stats",
#             description="Calculates and displays statistical analysis of the plants.",
#         )
#
#     def process(self):  # TODO unlimited args for param support to query
#         super().process()
#         db = Session()
#         plants: list[Plant] = db.query(Plant).all()
#
#         print(f"Totals: {len(plants)}")
#         print(f"Geni: {len(set([p.genus for p in plants]))}")
