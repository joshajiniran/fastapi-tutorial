# function
def check_phone_number_correct(phone: str):
    if phone.startswith('+234') and len(phone) == 14:
        return True
    
    if len(phone) == 11 and not phone.startswith('+234'):
        return True

    return False


# subroutine
def check_can_call_phone_number(phone: str):
    if phone.startswith('0805') or phone.startswith('0815') or phone.startswith('0807') or phone.startswith('0817'):
        print("Calls to this line are not allowed, please try other number!")
    else:
        print("Calling {}...".format(phone))
