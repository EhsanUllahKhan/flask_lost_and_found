class EmailAlreadyExistException(Exception):
    """
    Raised when email is already registered
    """
    def __init__(self, email):
        self.msg = "User with email: {email} already exists".format(email=email)

    def __str__(self):
        return self.msg

class UserDoesNotExistException(Exception):
    """
    Raised when email is not found
    """
    def __init__(self, email):
        self.msg = "User with email: {email} does not exist".format(email=email)

    def __str__(self):
        return self.msg



class ItemNotFoundException(Exception):
    """
        Raised when email is not found
    """
    def __init__(self, id):
        self.msg = "Item with id: {id} does not exist".format(id=id)

    def __str__(self):
        return self.msg