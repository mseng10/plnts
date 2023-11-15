from db import engine
from models.base import Base
from models.plant import Plant

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)