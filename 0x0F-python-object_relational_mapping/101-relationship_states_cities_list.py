#!/usr/bin/python3
"""
A script that lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}"
            )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects with corresponding City objects
    states = session.query(State).order_by(State.id).all()

    # Print State objects and corresponding City objects
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close session
    session.close()
