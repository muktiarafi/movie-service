from .custom_error import CustomError

class FieldValidatonError(CustomError):
    def __init__(self, message):
        errors = [' '.join(err) for err in message.items()]
        super().__init__(errors, 400, 'Not Found Error')