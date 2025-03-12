
class UserService:
    def __init__(self, user_repo):
        """初始化 UserService"""
        self.user_repo = user_repo

    def register(self, username):
        """註冊新使用者"""
        if self.user_repo.user_exists(username):
            return "Error - user already existing"
        self.user_repo.add_user(username)
        return "Success"

    def validate_user(self, username):
        """驗證使用者是否存在"""
        return self.user_repo.user_exists(username)
    
