from models.hardware_queries import check_registration, insert_pass


def is_registered(rf_id):
    """
    controller mvc func
    """
    return check_registration(rf_id)


def insert_data(rf_id):
    """
    controller mvc func
    """
    return insert_pass(rf_id)
