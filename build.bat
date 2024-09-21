# venv\Scripts\pyinstaller -y --clean --additional-hooks-dir extra-hooks --onefile --hidden-import=uvicorn --hidden-import=asyncpg.pgproto.pgproto --hidden-import=win32timezone --name=gdx2map_backend --workpath src  .\src\main.py

venv\Scripts\pyinstaller -y  ^
--clean  ^
--additional-hooks-dir extra-hooks  ^
--onefile  ^
--hidden-import=uvicorn  ^
--hidden-import=asyncpg.pgproto.pgproto ^
--hidden-import=win32timezone  ^
--name=gdx2map_backend  ^
.\src\main.py
