#!/usr/bin/python3
"""Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    argv = sys.argv
    argc = len(argv)

    if argc == 5:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        element = session.query(State).filter(State.name == '%s' %(argv[4],)).first()
        if element == None:
            print("Not found")
        else:
            print('{}: {}'.format(element.id, element.name))

        session.close()
