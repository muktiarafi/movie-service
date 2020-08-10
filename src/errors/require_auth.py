from .custom_error import CustomError

class RequireAuthError(CustomError):
    def __init__(self):
        super().__init__(['access not permitted'], 400, 'Authentication Error')