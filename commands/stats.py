from commands.command import Command
from util.db_util import DBUtil


class Stats(Command):
    def __init__(self):
        Command.__init__(
            self,
            key="stats",
            description="Calculates and displays statistical analysis of the plants.",
        )

    def process(self):  # TODO unlimited args for param support to query
        super().process()
        plants = DBUtil.read_plants()

        print(f"Totals: {len(plants)}")
        print(f"Geni: {len(set([p.genus for p in plants]))}")
