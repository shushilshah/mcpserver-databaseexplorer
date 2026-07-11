from sqlalchemy import text
from data.connection import get_engine


ALLOWED = [
    "SELECT",
    "WITH",
    "EXPLAIN"
]


def validate_query(sql):

    sql = sql.strip().upper()

    if not any(
        sql.startswith(cmd)
        for cmd in ALLOWED
    ):
        raise Exception(
            "Only read-only queries allowed"
        )


def execute_query(sql):

    validate_query(sql)

    with get_engine().connect() as conn:

        result = conn.execute(text(sql))

        return [
            dict(row._mapping)
            for row in result
        ]
