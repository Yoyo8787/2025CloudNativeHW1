

class CategoryService:
    def __init__(self, category_repo, listing_repo, user_service):
        """初始化 CategoryService"""
        self.category_repo = category_repo
        self.listing_repo = listing_repo
        self.user_service = user_service

    def add_listing_to_category(self, category, listing_id):
        """將商品加入分類"""
        listing = self.listing_repo.get_listing(listing_id)
        if listing:
            self.category_repo.add_listing_to_category(category, listing_id, listing["created_at"])

    def get_category_listings(self, username, category):
        """查詢分類內商品"""
        if not self.user_service.validate_user(username):
            return "Error - user not found"

        listing_ids = self.category_repo.get_category_listings(category)
        if isinstance(listing_ids, str):  # Error message from repo
            return listing_ids

        listings = [self.listing_repo.get_listing(lid) for lid in listing_ids]
        return "\n".join(
            f"{l['title']}|{l['description']}|{l['price']}|{l['created_at']}"
            for l in listings if l
        )

    def get_top_category(self, username):
        """取得擁有最多商品的分類"""
        if not self.user_service.validate_user(username):
            return "Error - user not found"

        top_category = self.category_repo.get_top_category()
        return top_category if top_category else "Error - no categories"
