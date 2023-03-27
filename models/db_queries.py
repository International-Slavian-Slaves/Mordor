import sqlite3 as sqlite
import sqlalchemy as db
from werkzeug.datastructures import ImmutableMultiDict
from models.count_month_time import create_stack, count_month_time
from models.db_model import person, passes

engine = db.create_engine("sqlite:///SQLite.db")


def make_dict(request_data):
    edited_data = ImmutableMultiDict.to_dict(request_data)
    data_dict = dict()
    data_dict['RF_ID'] = edited_data['rf_id']
    data_dict['Per_Fname'] = edited_data['f_name']
    data_dict['Per_Mname'] = edited_data['m_name']
    data_dict['Per_Lname'] = edited_data['l_name']
    return data_dict


def insert_person_data(request_data):
    with engine.connect() as connection:
        data_dict = make_dict(request_data)
        insertion_query = person.insert().values([data_dict])
        connection.execute(insertion_query)
        connection.commit()


def select_recent_passes(limit):
    with engine.connect() as connection:
        selection_query = db.select(person.join(passes, person.columns.RF_ID == passes.columns.RF_ID)) \
            .order_by(db.desc(passes.columns.Pass_Date))
        result = connection.execute(selection_query)
        return result.fetchmany(limit)


def select_locations():
    with sqlite.connect('SQLite.db') as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM GeneralViewDudes;"
        result = cursor.execute(query)
        return result.fetchall()


def select_month_time(id):
    with sqlite.connect('SQLite.db') as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM MonthPasses WHERE RF_ID = ?;"
        result = cursor.execute(query, (id,))
        data_array = result.fetchall()
        if data_array:
            stack = create_stack(data_array)
            return count_month_time(stack)
        else:
            return "Данные не найдены"


def select_admin(id):
    with engine.connect() as connection:
        selection_query = db.select(person) \
            .where(person.columns.RF_ID == id)
        result = connection.execute(selection_query)
        return result.fetchone()