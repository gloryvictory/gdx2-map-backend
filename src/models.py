# geo is based on example https://github.com/jgriffith23/postgis-tutorial/blob/master/model.py
# https://github.com/alvassin/alembic-quickstart/blob/master/staff/schema.py
# https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/
# from sqlalchemy import Table, mapped_column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT

from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (TIMESTAMP, Boolean, Integer, String, TEXT, BigInteger, Float)
# from sqlalchemy.dialects.postgresql import TSVECTOR

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from src.cfg import CONVENTION, DB_SCHEMA
from src.db.db import Base



class OrmBase(DeclarativeBase):
    # metadata = MetaData(naming_convention=CONVENTION)  # type: ignore
    metadata = MetaData(schema=DB_SCHEMA, naming_convention=CONVENTION)

    

class M_FIELD(Base):
    """A file table, including geospatial data for each file."""

    __tablename__ = 'field'
    __table_args__ = {'comment': 'Файлы'}
    # __table_args__ = {'schema': 'gdx2map'}
    # geom = Column(NullType)
    id:         Mapped[int] = mapped_column(primary_key=True)
    year:       Mapped[int] = mapped_column(BigInteger, nullable=True)
    tip:        Mapped[str] = mapped_column(String(length=10), nullable=True)
    areaoil:    Mapped[float] = mapped_column(Float, nullable=True)
    nom:        Mapped[int] = mapped_column(BigInteger, nullable=True)
    oil:        Mapped[str] = mapped_column(String(length=254), nullable=True)
    gas:        Mapped[str] = mapped_column(String(length=254), nullable=True)
    condensat:  Mapped[str] = mapped_column(String(length=254), nullable=True)
    name_ru:    Mapped[str] = mapped_column(String(length=254), nullable=True)
    oblast:     Mapped[str] = mapped_column(String(length=254), nullable=True)
    stadia:     Mapped[str] = mapped_column(String(length=254), nullable=True)
    note:       Mapped[str] = mapped_column(String(length=254), nullable=True)
    istochnik:  Mapped[str] = mapped_column(String(length=254), nullable=True)
    ftype:      Mapped[str] = mapped_column(String(length=8), nullable=True)
    
    
class M_LU(Base):
    """A file table, including geospatial data for each file."""

    __tablename__ = 'lu'
    __table_args__ = {'comment': 'Лицензионные участки'}
    
    id:         Mapped[int] = mapped_column(primary_key=True)
    areaoil:    Mapped[float] = mapped_column(Float, nullable=True)
    area_lic:   Mapped[str] = mapped_column(String(length=10), nullable=True)
    year:       Mapped[int] = mapped_column(BigInteger, nullable=True)
    nom_zsngp:  Mapped[int] = mapped_column(BigInteger, nullable=True)
    nom_list:   Mapped[str] = mapped_column(String(length=12), nullable=True)
    nom:        Mapped[int] = mapped_column(BigInteger, nullable=True)
    data_start: Mapped[str] = mapped_column(TIMESTAMP, nullable=True)  
    data_end:   Mapped[str] = mapped_column(TIMESTAMP, index=True, nullable=True)  
    vid:        Mapped[str] = mapped_column(String(length=50), nullable=True)
    ftype:      Mapped[str] = mapped_column(String(length=5), nullable=True)
    name_rus:   Mapped[str] = mapped_column(String(length=100), nullable=True)
    anumber:    Mapped[str] = mapped_column(String(length=10), nullable=True)
    sostiyanie: Mapped[str] = mapped_column(String(length=50), nullable=True)
    priznak:    Mapped[str] = mapped_column(String(length=50), nullable=True)
    nom_lic:    Mapped[str] = mapped_column(String(length=50), nullable=True)
    head_nedro: Mapped[str] = mapped_column(String(length=100), nullable=True)
    oblast:     Mapped[str] = mapped_column(String(length=100), nullable=True)
    zngp:       Mapped[str] = mapped_column(String(length=10), nullable=True)
    nedropolz:  Mapped[str] = mapped_column(String(length=150), nullable=True)
    nedropol:   Mapped[str] = mapped_column(String(length=100), nullable=True)
    nom_urfo:   Mapped[int] = mapped_column(BigInteger, nullable=True)
    authority:  Mapped[str] = mapped_column(String(length=254), nullable=True)
    
    
class M_STA(Base):
    __tablename__ = 'sta'
    __table_args__ = {'comment': 'Отчеты точки'}

    id:         Mapped[int] = mapped_column(primary_key=True)
    web_uk_id:  Mapped[str] = mapped_column(String(length=18), nullable=True)
    vid_iz:     Mapped[str] = mapped_column(String(length=26), nullable=True)
    tgf:        Mapped[str] = mapped_column(String(length=31), nullable=True)
    n_uk_tgf:   Mapped[str] = mapped_column(String(length=8), nullable=True)
    n_uk_rosg:  Mapped[str] = mapped_column(String(length=6), nullable=True)
    name_otch:  Mapped[str] = mapped_column(String(length=254), nullable=True)
    name_otch1: Mapped[str] = mapped_column(String(length=254), nullable=True)
    avts:       Mapped[str] = mapped_column(String(length=254), nullable=True)
    god_nach:   Mapped[str] = mapped_column(String(length=4), nullable=True)
    god_end:    Mapped[str] = mapped_column(String(length=4), nullable=True)
    org_isp:    Mapped[str] = mapped_column(String(length=193), nullable=True)
    in_n_tgf:   Mapped[str] = mapped_column(String(length=9), nullable=True)
    in_n_rosg:  Mapped[str] = mapped_column(String(length=10), nullable=True)
    nom_1000:   Mapped[str] = mapped_column(String(length=4), nullable=True)
    method:     Mapped[str] = mapped_column(String(length=13), nullable=True)
    scale:      Mapped[str] = mapped_column(String(length=26), nullable=True)
    


class M_STL(Base):
    __tablename__ = 'stl'
    __table_args__ = {'comment': 'Отчеты линии'}

    id:         Mapped[int] = mapped_column(primary_key=True)
    web_uk_id:  Mapped[str] = mapped_column(String(length=18), nullable=True)
    vid_iz:     Mapped[str] = mapped_column(String(length=26), nullable=True)
    tgf:        Mapped[str] = mapped_column(String(length=31), nullable=True)
    n_uk_tgf:   Mapped[str] = mapped_column(String(length=6), nullable=True)
    n_uk_rosg:  Mapped[str] = mapped_column(String(length=6), nullable=True)
    name_otch:  Mapped[str] = mapped_column(String(length=254), nullable=True)
    name_otch1: Mapped[str] = mapped_column(String(length=108), nullable=True)
    avts:       Mapped[str] = mapped_column(String(length=179), nullable=True)
    god_nach:   Mapped[str] = mapped_column(String(length=4), nullable=True)
    god_end:    Mapped[str] = mapped_column(String(length=4), nullable=True)
    org_isp:    Mapped[str] = mapped_column(String(length=192), nullable=True)
    in_n_tgf:   Mapped[str] = mapped_column(String(length=6), nullable=True)
    in_n_rosg:  Mapped[str] = mapped_column(String(length=6), nullable=True)
    nom_1000:   Mapped[str] = mapped_column(String(length=4), nullable=True)
    method:     Mapped[str] = mapped_column(String(length=13), nullable=True)
    scale:      Mapped[str] = mapped_column(String(length=26), nullable=True)


class M_STP(Base):
    __tablename__ = 'stp'
    __table_args__ = {'comment': 'Отчеты полигоны'}

    id:         Mapped[int] = mapped_column(primary_key=True)
    web_uk_id:  Mapped[str] = mapped_column(String(length=18), nullable=True)
    vid_iz:     Mapped[str] = mapped_column(String(length=26), nullable=True)
    tgf:        Mapped[str] = mapped_column(String(length=31), nullable=True)
    n_uk_tgf:   Mapped[str] = mapped_column(String(length=5), nullable=True)
    n_uk_rosg:  Mapped[str] = mapped_column(String(length=6), nullable=True)
    name_otch:  Mapped[str] = mapped_column(String(length=254), nullable=True)
    name_otch1: Mapped[str] = mapped_column(String(length=254), nullable=True)
    avts:       Mapped[str] = mapped_column(String(length=161), nullable=True)
    god_nach:   Mapped[str] = mapped_column(String(length=4), nullable=True)
    god_end:    Mapped[str] = mapped_column(String(length=4), nullable=True)
    org_isp:    Mapped[str] = mapped_column(String(length=190), nullable=True)
    in_n_tgf:   Mapped[str] = mapped_column(String(length=7), nullable=True)
    in_n_rosg:  Mapped[str] = mapped_column(String(length=6), nullable=True)
    nom_1000:   Mapped[str] = mapped_column(String(length=4), nullable=True)
    method:     Mapped[str] = mapped_column(String(length=13), nullable=True)
    scale:      Mapped[str] = mapped_column(String(length=26), nullable=True)

