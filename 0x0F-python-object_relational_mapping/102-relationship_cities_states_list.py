#!/usr/bin/python3
"""
use table relationship to access and print city and state
parameters given to script: username, password, database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(City).order_by(City.id).all()
    for city in rows:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
