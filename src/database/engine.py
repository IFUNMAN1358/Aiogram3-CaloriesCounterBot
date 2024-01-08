from os import environ
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()

engine = create_async_engine(environ.get('DB_URL'))
session = async_sessionmaker(engine)









