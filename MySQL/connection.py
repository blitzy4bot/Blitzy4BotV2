import os
import mysql.connector
import datetime
from dotenv import load_dotenv
load_dotenv()
passwd = os.getenv("PASSWD")
user = os.getenv("user")
database = os.getenv("database")

db = mysql.connector.connect(
    host="localhost",
    user=user,
    passwd=passwd,
    database=database
                            )


maincursor = db.cursor()


def commiting():
    db.commit()
    print(f"Saved changes at {datetime.datetime.now()}")