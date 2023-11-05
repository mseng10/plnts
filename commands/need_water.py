from datetime import datetime
from commands.auto import AutoCommand
from util.db_util import DBUtil


class NeedWaterCommand(AutoCommand):
    def __init__(self) -> None:
        AutoCommand.__init__(
            self,
            key="need_water",
            last_run=datetime.now().strftime("%m-%d-%Y"),
            inc=1,  # every day
        )

        def process(self) -> None:
            super().process()
            DBUtil.run_on_plants(self._process)

        def _process(self, plants):
            for plant in plants:
                if plant.needs_water():
                    print(f"{plant} needs water!")
