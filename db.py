from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME')

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    # Test connection
    with engine.begin() as conn:
        conn.execute("SELECT 1")
except exc.SQLAlchemyError as e:
    print(f"Failed to connect to the database: {e}")
    raise

Session = sessionmaker(bind=engine)

def get_db_connection():
    session = Session()
    try:
        yield session
    except exc.SQLAlchemyError as e:
        session.rollback()
        print(f"Database session error: {e}")
        raise
    finally:
        session.close()