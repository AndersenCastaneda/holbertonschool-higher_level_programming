#!/usr/bin/python3
"""Lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""


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
        query = session.query(State).filter(State.name.like('%a%'))
        for row in query.all():
            print('{}: {}'.format(row.id, row.name))

        session.close()
