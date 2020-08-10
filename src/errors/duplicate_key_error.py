from .custom_error import CustomError

class DuplicateKeyError(CustomError):
    def __init__(self, message):
        errors = [' '.format(err) for err in message.items()]
        super().__init__(errors, 400, 'Bad Request')