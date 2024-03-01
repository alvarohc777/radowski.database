import psycopg


from utils.dummy_data import (
    content_book_ii_eng,
    content_book_i_eng,
    content_poemas_para_mi_eng,
)
from utils import connection_strings
from utils import statements
from utils import utils as ut
from utils.dummy_data import poem_content_language

db_name = "radowski_dev2"
connection_string = connection_strings.AZURE
connection_string["dbname"] = db_name

insert_statement = statements.insert_statement


def batch_insert_content_eng(curs: psycopg.cursor):
    ut.generic_insert(curs, insert_statement, "content", content_book_i_eng)
    ut.generic_insert(curs, insert_statement, "content", content_book_ii_eng)
    ut.generic_insert(curs, insert_statement, "content", content_poemas_para_mi_eng)


with psycopg.connect(**connection_string) as conn:
    with conn.cursor() as curs:
        # batch_insert_content_eng(curs)
        # print(poem_content_language[44:])
        ut.generic_insert(
            curs, insert_statement, "poem_content_language", poem_content_language[44:]
        )
