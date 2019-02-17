from hashlib import sha256


def process_password(password):
    return str(sha256(password.encode()).hexdigest())


def is_email(email):
    if '@' in email and '.' in email:
        return True
    return False


def is_phone_number(data):
    try:
        data = int(data)
        if len(str(data)) == 10:
            return True
        return False
    except:
        return False
