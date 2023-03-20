from models.hardware_queries import check_registration


def is_registered(rf_id):
    return check_registration(rf_id)
