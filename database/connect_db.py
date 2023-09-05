from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url_to_db = 'postgresql+psycopg2://postgres:123456@localhost:5432/postgres'
engine = create_engine(url_to_db)
DBSession = sessionmaker(bind=engine)
session = DBSession()