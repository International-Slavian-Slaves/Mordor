import sqlalchemy as db
from models.db_model import person

engine = db.create_engine("sqlite:///SQLite.db")


def check_registration(rf_id):
    with engine.connect() as connection:
        selection_query = db.select(person).where(person.columns.RF_ID == rf_id)
        result = connection.execute(selection_query)
        if result.fetchall():
            return "True"
        else:
            return "False"
