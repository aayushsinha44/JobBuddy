from hashlib import sha256


def process_password(password):
    return str(sha256(password.encode()).hexdigest())
