from botactions.constants import ALLOWED_USER_ID_LIST


def verify_user(current_user_id):
    if current_user_id in list(ALLOWED_USER_ID_LIST):
        return True
    else:
        return False
