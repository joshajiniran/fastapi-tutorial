def check_phone_number_correct(phone: str):
    if len(phone) < 11 or len(phone) > 11:
        return False

    return True
