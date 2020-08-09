#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from model_city import City

    argv = sys.argv
    argc = len(argv)

    if argc == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        query = session.query(State, City).filter(
            City.state_id == State.id).order_by(City.id).all()
        for states, cities in query:
            print('{}: ({}) {}'.format(states.name, cities.id, cities.name))

        session.close()
