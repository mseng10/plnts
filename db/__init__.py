from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
import json

# TODO: May want to move db.json to __main__ as provided path
# This get's the job done for now and for awhile
with open("db/db.json") as json_data_file:
    db_config = json.load(json_data_file)

url = URL.create(
    drivername=db_config["drivername"],
    username=db_config["username"],
    password=db_config["password"],
    host=db_config["host"],
    database=db_config["database"],
    port=db_config["port"],
)

engine = create_engine(url)
connection = engine.connect()
Session = sessionmaker(bind=engine)
