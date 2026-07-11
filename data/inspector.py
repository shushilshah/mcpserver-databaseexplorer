from sqlalchemy import inspect
from data.connection import get_engine

def list_tables():
    inspector = inspect(get_engine())
    return inspector.get_table_names()


def get_schema(table_name):

    inspector = inspect(get_engine())

    columns = inspector.get_columns(table_name)

    return [
        {
            "name": c["name"],
            "type": str(c["type"])
        }
        for c in columns
    ]


def database_overview():
    inspector = inspect(get_engine())
    tables = inspector.get_table_names()
    total_columns = 0

    for table in tables:
        total_columns += len(inspector.get_columns(table))

        return {
            "tables": len(tables),
            "total_names": tables,
            "total_columns": total_columns
        }


def schema_context():
    inspector = inspect(get_engine())
    lines = []

    lines.append("Database Schema")
    lines.append("=" * 50)

    for table in inspector.get_table_names():
        lines.append(f"\nTable: {table}")
        lines.append("-" * 30)
        columns = inspector.get_columns(table)
        pk = inspector.get_pk_constraint(table)
        pk_columns = pk.get("constrained_columns", [])
        for column in columns:
            name = column['name']
            dtype = str(column['type'])
            suffix = ""

            if name in pk_columns:
                suffix = " (PRIMARY KEY)"

            lines.append(f"- {name}: {dtype}{suffix}")

    lines.append("\nRelationships")
    lines.append("-" * 30)

    for table in inspector.get_table_names():
        foriegn_keys = inspector.get_foreign_keys(table)
        for fk in foriegn_keys:
            lines.append(f"{table}.{fk['constrained_columns'][0]}"
                         f" -> "
                         f"{fk['referred_table']}.{fk['referred_columns'][0]}")
            
    return "\n".join(lines)