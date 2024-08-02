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

def build_db_connection_url():
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def initialize_database_engine():
    connection_url = build_db_connection_url()
    try:
        engine = create_engine(connection_url)
        with engine.begin() as connection:
            connection.execute("SELECT 1")
        return engine
    except exc.SQLAlchemyError as error:
        print(f"Failed to connect to the database: {error}")
        raise

database_engine = initialize_database_engine()
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