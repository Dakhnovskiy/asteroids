import hashlib


def get_hash(value: str):
    """
    generate hash by value
    :param value: string value
    """
    return hashlib.md5(value.encode()).hexdigest()
