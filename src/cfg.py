from dotenv import load_dotenv
import os
from time import strftime  # Load just the strftime Module from Time

load_dotenv()

API_VERSION = "/api/v1"

SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = os.getenv("SERVER_PORT", 8001)

DEVENV = os.getenv("DEVENV", "dev")

print(f"DEVENV: {DEVENV}")

if DEVENV.startswith("dev"):
    DB_HOST = os.getenv("DB_HOST", "localhost")
else:
    DB_HOST = os.getenv("DB_HOST", "r48-vldb02.zsniigg.local")
# DB_HOST = os.getenv("DB_HOST", "r48-vldb02.zsniigg.local")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "gdx2")
DB_SCHEMA = os.getenv("DB_SCHEMA", "gdx2")
DB_USER = os.getenv("DB_USER", "gdx2")
DB_PASS = os.getenv("DB_PASS", "gdx2pwd")
DB_DSN = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DB_DSN_ASYNCIO = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DB_DSN2 = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# print(DATABASE_URL)
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