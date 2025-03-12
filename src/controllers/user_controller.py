
class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def register(self, username):
        return self.user_service.register(username)
    
