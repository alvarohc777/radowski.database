import psycopg
import subprocess
from utils import connection_strings

db_name = "radowski_dev"

connection_string = connection_strings.AZURE
connection_string["dbname"] = db_name

# print(connection_string)

# with psycopg.connect(autocommit=True, **azure_connection_dict) as conn:
#     with conn.cursor() as cur:
#         cur.execute
