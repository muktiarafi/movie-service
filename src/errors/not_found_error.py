from .custom_error import CustomError

class NotFoundError(CustomError):
    def __init__(self):
        super().__init__(['Movie with that id does not found'], 400, 'Not Found Error')