from dotenv import load_dotenv
import os
from time import strftime  # Load just the strftime Module from Time

load_dotenv()

API_VERSION = "/api/v1"

DEVENV = os.getenv("DEVENV", "dev")

SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = os.getenv("SERVER_PORT", 8082)

DB_DSN_ENV = ""

if DEVENV.startswith("dev"):
    DB_DSN_ENV = os.getenv("GDX2MAP_DB_DSN", "postgresql://gdx2map:gdx2mappwd@localhost:5432/gdx2map?sslmode=disable")
else:
    DB_DSN_ENV = os.getenv("GDX2MAP_DB_DSN", "postgresql://gdx2map:gdx2mappwd@r48-vldb02.zsniigg.local:5432/gdx2map?sslmode=disable")

DB_SCHEMA = os.getenv("GDX2MAP_SCHEMA", "gdx2map")
DB_DSN = DB_DSN_ENV.replace("postgresql://", "postgresql+asyncpg://")
DB_DSN2 = DB_DSN_ENV.replace("postgresql://", "postgresql+psycopg2://") 

DATETIME_CURRENT = str(strftime("%Y-%m-%d-%H-%M-%S"))

CONVENTION = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

CRS_OUT = 4326  # 4326 - WGS 84

MSG_OK = "OK"
MSG_ERROR = "ERROR"

print(f"DEVENV: {DEVENV}")
print(f"SERVER_HOST: {SERVER_HOST}")
print(f"SERVER_PORT: {SERVER_PORT}")
print(f"DB_DSN: {DB_DSN}")
print(f"DB_DSN2 for alembic: {DB_DSN2}")
print(f"http://{SERVER_HOST}:{SERVER_PORT}/docs")

# DB_HOST = os.getenv("DB_HOST", "r48-vldb02.zsniigg.local")
# DB_HOST = os.getenv("DB_HOST", "r48-vldb02.zsniigg.local")
# DB_PORT = os.getenv("DB_PORT", 5432)
# DB_NAME = os.getenv("DB_NAME", "gdx2")
# DB_USER = os.getenv("DB_USER", "gdx2")
# DB_PASS = os.getenv("DB_PASS", "gdx2pwd")
# db_dsn_tmp = DB_DSN_ENV.replace("postgresql://", "postgresql+asyncpg://")
# DB_DSN = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DB_DSN_ASYNCIO = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DB_DSN2 = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
