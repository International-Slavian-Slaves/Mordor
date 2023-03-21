from models.hardware_queries import check_registration, insert_pass


def is_registered(rf_id):
    return check_registration(rf_id)

def insert_data(rf_id):
    return insert_pass(rf_id)