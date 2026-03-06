#!/usr/bin/python3
"""
delete states that contain the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3],),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute(delete(State).where(State.name.contains('a'))
                    .execution_options(synchronize_session="fetch"))
    session.commit()
    session.close()
