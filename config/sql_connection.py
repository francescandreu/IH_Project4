import sqlalchemy as alch
import os
from dotenv import load_dotenv

load_dotenv()

dbName = "movies"
password = os.getenv("SQL_password")

connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)