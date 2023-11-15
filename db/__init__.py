from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

url = URL.create(
        drivername="postgresql",
        username="",
        password="",
        host="localhost",
        database="plnts",
        port=5432
    )

engine = create_engine(url)
connection = engine.connect()
Session = sessionmaker(bind=engine)