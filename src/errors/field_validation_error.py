from .custom_error import CustomError

class FieldValidationError(CustomError):
    def __init__(self, message):
        errors = ['{} {}'.format(err[0], err[1][0]) for err in message.items()]
        super().__init__(errors, 400, 'Bad Request')