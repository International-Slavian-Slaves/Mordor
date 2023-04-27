from models.db_queries import insert_person_data, select_recent_passes, select_locations, select_month_time
from models.db_queries import select_admin
from models.kill_yourself import make_fun


def register_user(request_data):
    """
    controller mvc func
    """
    insert_person_data(request_data)


def get_recent_passes(limit):
    """
    controller mvc func
    """
    return select_recent_passes(limit)


def get_fun():
    """
    controller mvc func
    """
    return make_fun()


def get_locations():
    """
    controller mvc func
    """
    return select_locations()


def get_hours(id):
    """
    controller mvc func
    """
    return select_month_time(id)


def check_admin(id):
    """
    controller mvc func
    """
    return select_admin(id)
