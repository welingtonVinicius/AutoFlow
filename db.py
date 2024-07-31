from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DATABASE_USER')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')
DB_HOST = os.getenv('DATABASE_HOST')
DB_PORT = os.getenv('DATABASE_PORT', '5432')
DB_NAME = os.getenv('DATABASE_NAME')

DB_CONNECTION_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    database_engine = create_engine(DB_CONNECTION_URL)
    with database_engine.begin() as connection:
        connection.execute("SELECT 1")
except exc.SQLAlchemyError as error:
    print(f"Failed to connect to the database: {error}")
    raise

DatabaseSession = sessionmaker(bind=database_engine)

def get_database_session():
    session = DatabaseSession()
    try:
        yield session
    except exc.SQLAlchemyError as error:
        session.rollback()
        print(f"Database session error: {error}")
        raise
    finally:
        session.close()