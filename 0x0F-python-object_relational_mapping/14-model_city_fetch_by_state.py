#!/usr/bin/python3
"""
Link class to a table in the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]
    State.cities = relationship("City",
                                order_by=City.id, back_populates="state")
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection.format(user_name, password, db_name),
                            pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    model_city = session.query(State, City)\
        .filter(City.state_id == State.id).all()

    for data in model_city:
        print("{}: ({}) {}".format(data[0].name, data[1].id, data[1].name))
