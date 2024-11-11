import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import AnnualWage, AnnualWagesPlayers, SquadValue, TransferSpending, LeagueTable,Base
from dotenv import load_dotenv
from transfer_spendings import final_data
from league_table_scrapper import league_table

load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
hostname = os.getenv('DB_HOSTNAME')
database_name = os.getenv('DB_NAME')


engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}/{database_name}')
Session = sessionmaker(bind=engine)


if __name__ == '__main__':

    Base.metadata.create_all(engine)
    with Session() as session:
        session.bulk_save_objects(final_data)
        session.commit()
        print(session.query(TransferSpending).all())


