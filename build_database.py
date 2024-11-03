import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import AnnualWage, AnnualWagesPlayers, SquadValue, TransferSpending
from dotenv import load_dotenv
from transfer_spendings import final_data

load_dotenv()
user = 'postgres'
password = 1111
hostname = 'localhost'
database_name = 'football_salaries'

Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}/{database_name}')
Session = sessionmaker(bind=engine)


if __name__ == '__main__':

    Base.metadata.create_all(engine)
    with Session() as session:
        session.bulk_save_objects(final_data)
        session.commit()
        print(session.query(TransferSpending).all())


