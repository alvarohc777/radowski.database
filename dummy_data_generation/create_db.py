import psycopg
import subprocess

from utils import connection_strings

db_name = "radowski_dev"

connection_string = connection_strings.AZURE

with psycopg.connect(autocommit=True, **connection_string) as conn:
    with conn.cursor() as cur:
        cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cur.execute(f"CREATE DATABASE {db_name}")

psql_restore_cmd = "psql -U alvarohc777 -h radowski.postgres.database.azure.com -d radowski_dev -W -f ./schemas/radowskiDev.sql"

powershell_command = "powershell.exe"
subprocess.run(f"{powershell_command} -c {psql_restore_cmd}", shell=True)


# subprocess.run(psql_restore_cmd)
