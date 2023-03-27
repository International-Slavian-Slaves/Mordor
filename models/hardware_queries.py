import sqlalchemy as db
from models.db_model import person, passes
import sqlite3 as sqlite
from datetime import datetime

engine = db.create_engine("sqlite:///SQLite.db")


def check_registration(rf_id):
    with engine.connect() as connection:
        selection_query = db.select(person).where(person.columns.RF_ID == rf_id)
        result = connection.execute(selection_query)
        if result.fetchall():
            return "True"
        else:
            return "False"


def insert_pass(rf_id):
    time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    location = get_location(rf_id)
    if location is None:
        return
    if get_location(rf_id)[0] == "Внутри":
        direction = "out"
    else:
        direction = "in"
    with engine.connect() as connection:
        #insertion_query = passes.insert().values((rf_id, time, direction))
        insertion_query = passes.insert().values({'RF_ID': rf_id, 'Pass_Date': time, 'Pass_Dir': direction})
        connection.execute(insertion_query)
        connection.commit()


def get_location(rf_id):
    with sqlite.connect('SQLite.db') as connection:
        cursor = connection.cursor()
        query = "SELECT WhereNow FROM GeneralViewDudes WHERE RF_ID = ?;"
        result = cursor.execute(query, (rf_id,))
        return result.fetchone()
