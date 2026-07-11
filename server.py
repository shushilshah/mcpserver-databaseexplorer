from mcp.server.fastmcp import FastMCP
from data.inspector import (list_tables, get_schema, database_overview, schema_context)
from data.query_executor import execute_query

mcp = FastMCP("Database Explorer")

@mcp.tool()
def hello():
    return "Hello, World"

@mcp.tool()
def get_tables():
    """
    Return all database tables
    """
    return list_tables()

@mcp.tool()
def describe_table(table_name: str):
    """
    Return table schema for a given table
    """
    return get_schema(table_name)

@mcp.tool()
def query(sql: str):
    """
    Execute read only queries
    """
    return execute_query(sql)

@mcp.tool()
def overview():
    """
    High level database summary.
    """
    return database_overview()


@mcp.tool()
def schema():
    """
    return the complete database schema in a human readable format"""

    return schema_context()

if __name__ == "__main__":
    mcp.run()
