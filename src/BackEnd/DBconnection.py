from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

class PostgresConnection:

    def __init__(self, user: str, password: str, host: str, port: int, database_name: str):
        try:
            self.engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database_name}")
            self.session = sessionmaker(bind=self.engine)
        except SQLAlchemyError as e:
            print(f"Error connecting to database: {e}")
