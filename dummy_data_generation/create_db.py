import psycopg
import subprocess

from utils import connection_strings

# db_name = "radowski_dev"
db_name = "radowski_dev2"
sql_file = "radowskiDev2.sql"

connection_string = connection_strings.AZURE

with psycopg.connect(autocommit=True, **connection_string) as conn:
    with conn.cursor() as cur:
        cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cur.execute(f"CREATE DATABASE {db_name}")

psql_restore_cmd = f"psql -U alvarohc777 -h radowski.postgres.database.azure.com -d {db_name} -W -f ./schemas/{sql_file}"

powershell_command = "powershell.exe"
subprocess.run(f"{powershell_command} -c {psql_restore_cmd}", shell=True)


# subprocess.run(psql_restore_cmd)
