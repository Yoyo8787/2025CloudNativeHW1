
class ListingService:
    def __init__(self, listing_repo, user_service, category_service):
        """初始化 ListingService"""
        self.listing_repo = listing_repo
        self.user_service = user_service
        self.category_service = category_service

    def create_listing(self, username, title, description, price, category):
        """新增商品"""
        if not self.user_service.validate_user(username):
            return "Error - user not found"

        listing_id = self.listing_repo.add_listing(username, title, description, price, category)
        self.category_service.add_listing_to_category(category, listing_id)
        # 確保返回的是數字格式的字符串
        return str(listing_id)

    def get_listing(self, username, listing_id):
        """取得商品資訊"""
        if not self.user_service.validate_user(username):
            return "Error - user not found"

        listing = self.listing_repo.get_listing(listing_id)
        if not listing:
            return "Error - not found"

        return f"{listing['title']}|{listing['description']}|{listing['price']}|{listing['created_at']}|{listing['category']}|{listing['username']}"

    def delete_listing(self, username, listing_id):
        """刪除商品（檢查擁有權）"""
        return self.listing_repo.delete_listing(username, listing_id)
