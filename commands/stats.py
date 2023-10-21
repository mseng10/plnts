from commands.command import Command
from util.db_util import DBUtil
class Stats(Command):

    def __int__(self):
        super().__init__('stats')
    def process(self): # TODO unlimited args for param support to query
        plants = DBUtil.read_plants()

        # geni = set([p.genus for p in plants])
        # plants_map = {}
        #
        # for p in plants:
        #     if p['grade'] not in grouped_grades:
        #         plants_map[p['grade']] = []
        #
        #     grouped_grades[item['grade']].append(item)

        print(f"Totals: {len(plants)}")
        print(f"Geni: {len(set([p.genus for p in plants]))}")

