from commands.command import Command
from datetime import datetime, timedelta


class AutoCommand(Command):
    def __init__(self, key: str, last_run: str, inc: int) -> None:  # duh
        self.last_run: str = last_run
        self.inc: int = inc
        Command.__init__(self, key=key)

    def ready(self, curr_time) -> bool:
        return (
            datetime.strptime(self.last_run, "%m-%d-%Y") + timedelta(days=self.inc)
            >= curr_time
        )

    def process(self) -> None:
        super().process()
        self.last_run: str = datetime.now().strftime("%m-%d-%Y")
