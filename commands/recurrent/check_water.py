from datetime import datetime
from commands.recurrent.recurrent import Recurrent
from models.plant import Plant
from db import Session

class CheckWater(Recurrent):
    def __init__(self) -> None:
        Recurrent.__init__(
            self,
            key="need_water",
            description="Checks and displays plants that need water.",
            last_run=datetime.now().strftime("%m-%d-%Y"),
            inc=1,  # every day
        )

    def process(self) -> None:
        Recurrent.process(self)
        db = Session()
        plants: list[Plant] = db.query(Plant).all()
        for plant in plants:
            if plant.needs_water():
                print(f"{plant} needs water!")
