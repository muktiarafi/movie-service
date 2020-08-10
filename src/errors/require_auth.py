from .custom_error import CustomError

class RequireAuthError(CustomError):
    def __init__(self):
        super().__init__(['Not authorized'], 400, 'Unauthorized')