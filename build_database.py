from sqlalchemy import Double, create_engine
from sqlalchemy.orm import mapped_column, Mapped, relationship, sessionmaker, declarative_base
from scrapper import list_of_teams
from scrapper_squad_values import data

user = 'postgres'
password = '1111'
hostname = 'localhost'
database_name = 'football_salaries'

Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}/{database_name}')
Session = sessionmaker(bind=engine)

class AnnualWage(Base):

    __tablename__ = 'Annual Wage'

    id:Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    team:Mapped[str]
    season:Mapped[str]
    weekly_salary:Mapped[float]
    annual_wage:Mapped[float]

class SquadValue(Base):

    __tablename__ = 'Squad Value'

    id:Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    team:Mapped[str]
    season:Mapped[str]
    squad_member:Mapped[int]
    average_age:Mapped[float]
    average_player_value:Mapped[float]
    squad_value:Mapped[float]


if __name__ == '__main__':

    Base.metadata.create_all(engine)

    list_of_objects_teams = []
    list_squad_value = []

    '''for i in range(len(list_of_teams)):
        club = AnnualWage(team=list_of_teams[i]['Team'], season=list_of_teams[i]['Season'], weekly_salary = list_of_teams[i]['Weekly Salary'], 
                          annual_wage= list_of_teams[i]['Annual Salary'])
        list_of_objects_teams.append(club)'''
    
    for i in range(len(data)):
        club_value = SquadValue(team=data[i]['Team'], season=data[i]['Season'], squad_member=data[i]['Squad'], average_age=data[i]['Average age'],
                                average_player_value=data[i]['Average player value'], squad_value=data[i]['Squad value'])
        list_squad_value.append(club_value)

    with Session() as session:
        session.bulk_save_objects(list_squad_value)
        session.commit()
        print(session.query(SquadValue).all())


