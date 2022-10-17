from app.core import Loader
from dotenv import dotenv_values
import pandas as pd

env = dotenv_values()


class SQLServerConnection:
    engine = None

    def get_engine():
        if SQLServerConnection.engine is None:
            from sqlalchemy import create_engine
            from sqlalchemy.engine import URL

            DATABASE_URL = env["DATABASE_URL_SQL_SERVER"]
            conn = URL.create("mssql+pyodbc", DATABASE_URL, query={"odbc_connect": DATABASE_URL})
            SQLServerConnection.engine = create_engine(conn)

        return SQLServerConnection.engine


class RepositoryTest(Loader, SQLServerConnection):
    def __init__(self) -> None:
        self.engine = SQLServerConnection.get_engine()

    async def load(self, inputs=None):
        query = "SELECT TOP 10 codcli AS codcli FROM e085cli"

        DF = list(pd.read_sql_query(query, self.engine).T.to_dict().values())

        return DF
