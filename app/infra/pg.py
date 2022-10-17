from app.core import Adder, Checker, Loader
from dotenv import dotenv_values
import pandas as pd

env = dotenv_values()


class PostgresConnection:
    engine = None

    def get_engine():
        if PostgresConnection.engine is None:
            from sqlalchemy import create_engine
            from sqlalchemy.engine import URL

            DATABASE_URL = env["DATABASE_URL_POSTGRES"]
            PostgresConnection.engine = create_engine(DATABASE_URL)

        return PostgresConnection.engine

    def query(query, engine):
        df = list(pd.read_sql_query(query, engine).T.to_dict().values())

        return df[0] if len(df) > 0 else None


class AddUserPg(Adder):
    def __init__(self):
        self.engine = PostgresConnection.get_engine()

    async def add(self, inputs):
        query = f"""
            INSERT INTO 
                users (email, password, username) 
            VALUES 
                ('{inputs["email"]}', '{inputs["password"]}', '{inputs["username"]}')
            RETURNING id_user
        """
        DF = PostgresConnection.query(query, self.engine)

        return DF


class CheckExistEmailPg(Checker):
    def __init__(self):
        self.engine = PostgresConnection.get_engine()

    async def check(self, email: str) -> bool:
        query = f"SELECT COUNT(*) AS count FROM users WHERE email = '{email}'"

        DF = PostgresConnection.query(query, self.engine)

        return True if DF["count"] > 0 else False


class LoadUserByEmail(Loader):
    def __init__(self):
        self.engine = PostgresConnection.get_engine()

    async def load(self, email: str):
        query = f"SELECT * FROM users WHERE email = '{email}'"

        DF = PostgresConnection.query(query, self.engine)

        return DF


class LoadUserById(Loader):
    def __init__(self):
        self.engine = PostgresConnection.get_engine()

    async def load(self, id_user: int):
        query = f"SELECT * FROM users WHERE id_user = {id_user}"

        DF = PostgresConnection.query(query, self.engine)

        return DF
