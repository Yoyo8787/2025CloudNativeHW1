
class CategoryController:
    def __init__(self, category_service):
        self.category_service = category_service

    def get_category(self, username, category):
        return self.category_service.get_category_listings(username, category)

    def get_top_category(self, username):
        return self.category_service.get_top_category(username)
