
class CategoryController:
    def __init__(self, category_service):
        self.category_service = category_service

    def get_category(self, username, category):
        return self.category_service.get_category_listings(username, category)

    def get_top_category(self, username):
        top_categories = self.category_service.get_top_category(username)
        
        if isinstance(top_categories, str):  # 如果返回的是錯誤訊息（如 "Error - user not found"）
            return top_categories
        
        # 將分類名稱逐行顯示
        return "\n".join(top_categories)
