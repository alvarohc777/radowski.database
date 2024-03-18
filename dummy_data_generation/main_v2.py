import psycopg
from utils import dummy_data_schema_2 as dt
from utils import statements
from utils import utils as ut
from utils import connection_strings

db_name = "radowski_dev"

connection_string = connection_strings.AZURE_FINALE_APP
print(connection_string)
connection_string["dbname"] = db_name
print(connection_string)

insert_statement = statements.insert_statement


def batch_insert(cur: psycopg.cursor):
    ut.generic_insert(cur, insert_statement, "language", dt.language)
    ut.generic_insert(cur, insert_statement, "book", dt.book)
    ut.generic_insert(cur, insert_statement, "poem", dt.poem)
    ut.generic_insert(cur, insert_statement, "content", dt.content)
    ut.generic_insert(cur, insert_statement, "book_content", dt.book_content)
    ut.generic_insert(cur, insert_statement, "content_image", dt.content_image)


def batch_delete(cur: psycopg.cursor):
    # Stage 3
    ut.generic_delete(cur, "book_content")
    ut.generic_delete(cur, "content_image")
    ut.generic_delete(cur, "language")
    ut.generic_delete(cur, "book")
    ut.generic_delete(cur, "poem")
    ut.generic_delete(cur, "content_image")


with psycopg.connect(**connection_string) as conn:
    with conn.cursor() as cur:
        pass
        # Insert Statements

        # ut.generic_delete(cur, "book_content")
        # ut.generic_insert(cur, insert_statement, "book_content", dt.book_content)
        batch_delete(cur)
        batch_insert(cur)

        # conn.commit()
