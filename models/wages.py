from sqlalchemy.orm import mapped_column, Mapped, relationship, sessionmaker, declarative_base

Base = declarative_base()

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

class AnnualWagesPlayers(Base):

    __tablename__ = 'Annual Wage Players'

    id:Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    season:Mapped[str]
    player_name:Mapped[str]
    age:Mapped[int]
    team:Mapped[str]
    nationality:Mapped[str]
    position:Mapped[str]
    weekly_salary:Mapped[float]
    annual_salary:Mapped[float]