from datetime import datetime
from commands.auto.auto import AutoCommand
from models.plant import Plant
from util.db_util import DBUtil


class NeedWaterCommand(AutoCommand):
    def __init__(self) -> None:
        AutoCommand.__init__(
            self,
            key="need_water",
            description="Checks and displays plants that need water.",
            last_run=datetime.now().strftime("%m-%d-%Y"),
            inc=1,  # every day
        )

        def process(self) -> None:
            AutoCommand.process(self)
            DBUtil.update_plants(self._process)

        def _process(self, plants: list[Plant]) -> None:
            for plant in plants:
                if plant.needs_water():
                    print(f"{plant} needs water!")
