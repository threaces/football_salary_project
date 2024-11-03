import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import AnnualWage, AnnualWagesPlayers, SquadValue
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
hostname = os.getenv('DB_HOSTNAME')
database_name = os.getenv('DB_NAME')

Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}/{database_name}')
Session = sessionmaker(bind=engine)


if __name__ == '__main__':

    #Base.metadata.create_all(engine)

    '''for i in range(len(list_of_teams)):
        club = AnnualWage(team=list_of_teams[i]['Team'], season=list_of_teams[i]['Season'], weekly_salary = list_of_teams[i]['Weekly Salary'], 
                          annual_wage= list_of_teams[i]['Annual Salary'])
        list_of_objects_teams.append(club)'''
    
    '''for i in range(len(data)):
        club_value = SquadValue(team=data[i]['Team'], season=data[i]['Season'], squad_member=data[i]['Squad'], average_age=data[i]['Average age'],
                                average_player_value=data[i]['Average player value'], squad_value=data[i]['Squad value'])
        list_squad_value.append(club_value)'''
    
    '''for i in range(len(list_of_teams)):
        player = AnnualWagesPlayers(season=list_of_teams[i]['Season'], player_name=list_of_teams[i]['Player Name'], age=list_of_teams[i]['Age'],
                                     team=list_of_teams[i]['Club'], nationality=list_of_teams[i]['Nationality'], position=list_of_teams[i]['Position'],
                                     weekly_salary=list_of_teams[i]['Weekly Salary'], annual_salary=list_of_teams[i]['Annual Salary'])
        list_players_salary.append(player)

    with Session() as session:
        session.bulk_save_objects(list_players_salary)
        session.commit()
        print(session.query(AnnualWagesPlayers).all())'''


