import psycopg
from utils import dummy_data
from utils import statements
from utils import utils as ut
from utils import connection_strings

db_name = "radowski_dev"

connection_string = connection_strings.AZURE
print(connection_string)
connection_string["dbname"] = db_name
print(connection_string)

insert_statement = statements.insert_statement


def batch_insert(curr: psycopg.cursor):
    ut.generic_insert(cur, insert_statement, "poem", dummy_data.poem)
    ut.generic_insert(cur, insert_statement, "language", dummy_data.language)
    ut.generic_insert(cur, insert_statement, "book", dummy_data.book)
    ut.generic_insert(
        cur, insert_statement, "poem_book_language", dummy_data.poem_book_language
    )
    ut.generic_insert(cur, insert_statement, "content", dummy_data.content)
    ut.generic_insert(
        cur, insert_statement, "poem_content_language", dummy_data.poem_content_language
    )


def batch_delete(cur: psycopg.cursor):
    # Stage 3
    ut.generic_delete(cur, "poem_book_language")
    ut.generic_delete(cur, "poem_content_language")
    ut.generic_delete(cur, "language")
    ut.generic_delete(cur, "poem")
    ut.generic_delete(cur, "book")
    ut.generic_delete(cur, "content")


with psycopg.connect(**connection_string) as conn:
    with conn.cursor() as cur:
        pass
        # Insert Statements

        batch_delete(cur)
        batch_insert(cur)

        # conn.commit()
