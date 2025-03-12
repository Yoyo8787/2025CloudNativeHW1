class UserRepository:
    def __init__(self):
        """初始化用戶資料存儲"""
        self.users = {}

    def user_exists(self, username):
        """檢查使用者是否存在（不區分大小寫）"""
        return username.lower() in [user.lower() for user in self.users.keys()]

    def add_user(self, username):
        """新增使用者"""
        if not self.user_exists(username):
            self.users[username] = username  # 保持原始大小寫
        else:
            print(f"使用者 {username} 已存在。")

    def get_all_users(self):
        """獲取所有使用者列表"""
        return list(self.users.values())
