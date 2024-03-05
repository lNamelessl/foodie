from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    """This function hashes a password

    Args:
        password (str): The user password

    Returns:
        dict[str]: The hashed password
    """
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    """This function verfies a password

    Returns:
        dict[str]: The verified password
    """
    return pwd_context.verify(plain_password, hashed_password)
