# coding: utf-8
from sqlalchemy import BigInteger, CheckConstraint, Column, Date, Float, Integer, String, Table, Text, text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Field(Base):
    __tablename__ = 'field'
    __table_args__ = {'schema': 'gdx2map'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"gdx2map\".field_id_seq'::regclass)"))
    geom = Column(NullType)
    year = Column(BigInteger)
    tip = Column(String(10))
    areaoil = Column(Float(53))
    nom = Column(BigInteger)
    oil = Column(String(254))
    gas = Column(String(254))
    condensat = Column(String(254))
    name_ru = Column(String(254))
    oblast = Column(String(254))
    stadia = Column(String(254))
    note = Column(String(254))
    istochnik = Column(String(254))
    ftype = Column(String(8))


t_geography_columns = Table(
    'geography_columns', metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text),
    schema='gdx2map'
)


t_geometry_columns = Table(
    'geometry_columns', metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30)),
    schema='gdx2map'
)


class Lu(Base):
    __tablename__ = 'lu'
    __table_args__ = {'schema': 'gdx2map'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"gdx2map\".lu_id_seq'::regclass)"))
    geom = Column(NullType)
    areaoil = Column(Float(53))
    area_lic = Column(String(10))
    year = Column(BigInteger)
    nom_zsngp = Column(BigInteger)
    nom_list = Column(String(12))
    nom = Column(BigInteger)
    data_start = Column(Date)
    data_end = Column(Date)
    vid = Column(String(50))
    ftype = Column(String(5))
    name_rus = Column(String(100))
    anumber = Column(String(10))
    sostiyanie = Column(String(50))
    priznak = Column(String(50))
    nom_lic = Column(String(50))
    head_nedro = Column(String(100))
    oblast = Column(String(100))
    zngp = Column(String(10))
    nedropolz = Column(String(150))
    nedropol = Column(String(100))
    nom_urfo = Column(BigInteger)
    authority = Column(String(254))


class SpatialRefSy(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = (
        CheckConstraint('(srid > 0) AND (srid <= 998999)'),
        {'schema': 'gdx2map'}
    )

    srid = Column(Integer, primary_key=True)
    auth_name = Column(String(256))
    auth_srid = Column(Integer)
    srtext = Column(String(2048))
    proj4text = Column(String(2048))


class Sta(Base):
    __tablename__ = 'sta'
    __table_args__ = {'schema': 'gdx2map'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"gdx2map\".sta_id_seq'::regclass)"))
    geom = Column(NullType)
    web_uk_id = Column(String(18))
    vid_iz = Column(String(26))
    tgf = Column(String(31))
    n_uk_tgf = Column(String(8))
    n_uk_rosg = Column(String(6))
    name_otch = Column(String(254))
    name_otch1 = Column(String(254))
    avts = Column(String(254))
    god_nach = Column(String(4))
    god_end = Column(String(4))
    org_isp = Column(String(193))
    in_n_tgf = Column(String(9))
    in_n_rosg = Column(String(10))
    nom_1000 = Column(String(4))
    method = Column(String(13))
    scale = Column(String(26))


class Stl(Base):
    __tablename__ = 'stl'
    __table_args__ = {'schema': 'gdx2map'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"gdx2map\".stl_id_seq'::regclass)"))
    geom = Column(NullType)
    web_uk_id = Column(String(18))
    vid_iz = Column(String(26))
    tgf = Column(String(31))
    n_uk_tgf = Column(String(6))
    n_uk_rosg = Column(String(6))
    name_otch = Column(String(254))
    name_otch1 = Column(String(108))
    avts = Column(String(179))
    god_nach = Column(String(4))
    god_end = Column(String(4))
    org_isp = Column(String(192))
    in_n_tgf = Column(String(6))
    in_n_rosg = Column(String(6))
    nom_1000 = Column(String(4))
    method = Column(String(13))
    scale = Column(String(26))


class Stp(Base):
    __tablename__ = 'stp'
    __table_args__ = {'schema': 'gdx2map'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"gdx2map\".stp_id_seq'::regclass)"))
    geom = Column(NullType)
    web_uk_id = Column(String(18))
    vid_iz = Column(String(26))
    tgf = Column(String(31))
    n_uk_tgf = Column(String(5))
    n_uk_rosg = Column(String(6))
    name_otch = Column(String(254))
    name_otch1 = Column(String(254))
    avts = Column(String(161))
    god_nach = Column(String(4))
    god_end = Column(String(4))
    org_isp = Column(String(190))
    in_n_tgf = Column(String(7))
    in_n_rosg = Column(String(6))
    nom_1000 = Column(String(4))
    method = Column(String(13))
    scale = Column(String(26))
