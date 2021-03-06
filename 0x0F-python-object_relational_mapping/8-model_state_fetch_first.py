#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    argv = sys.argv
    argc = len(argv)

    if argc == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        first = session.query(State).first()

        if first is None:
            print("Nothing")
        else:
            print('{}: {}'.format(first.id, first.name))

        session.close()
