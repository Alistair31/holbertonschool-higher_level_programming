#!/usr/bin/python3
"""
update the name of a state in the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3],),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    change_state = State(name="New Mexico")
    session.execute(update(State).where(State.id == 2)
                    .values(name=change_state.name))
    session.commit()
    session.close()
