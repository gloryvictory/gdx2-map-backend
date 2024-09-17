# geo is based on example https://github.com/jgriffith23/postgis-tutorial/blob/master/model.py
# https://github.com/alvassin/alembic-quickstart/blob/master/staff/schema.py
# https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/
# from sqlalchemy import Table, mapped_column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT

# from datetime import datetime
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy import (TIMESTAMP, Boolean, Integer, String, TEXT, BigInteger, Float)
# from sqlalchemy.dialects.postgresql import TSVECTOR

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

# from src.db.db import Base

from src.cfg import cfg

class OrmBase(DeclarativeBase):
    metadata = MetaData(naming_convention=cfg.CONVENTION)  # type: ignore