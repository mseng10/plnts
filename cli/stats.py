from models.plant import Plant
from app import app, Session

@app.cli.command("stats")
def process(self):  # TODO unlimited args for param support to query
    super().process()
    db = Session()
    plants: list[Plant] = db.query(Plant).all()

    print(f"Totals: {len(plants)}")
    print(f"Geni: {len(set([p.genus for p in plants]))}")
