import time

class ListingRepository:
    def __init__(self):
        """初始化商品儲存與 ID 計數器"""
        self.listings = {}
        self.next_id = 100000  # 從 100000 開始分配 ID

    def add_listing(self, username, title, description, price, category):
        """新增商品，並自動產生 listing_id"""
        self.next_id += 1
        listing_id = self.next_id
        created_at = time.strftime("%Y-%m-%d %H:%M:%S")

        self.listings[listing_id] = {
            "title": title,
            "description": description,
            "price": price,
            "category": category,
            "username": username,
            "created_at": created_at
        }
        return listing_id

    def get_listing(self, listing_id):
        """根據 listing_id 獲取商品資訊"""
        return self.listings.get(listing_id, None)

    def delete_listing(self, username, listing_id):
        """刪除商品，確保只有商品擁有者能刪除"""
        if listing_id not in self.listings:
            return "Error - listing does not exist"

        if self.listings[listing_id]["username"] != username:
            return "Error - listing owner mismatch"

        del self.listings[listing_id]
        return "Success"

    def get_all_listings(self):
        """獲取所有商品（可擴展功能）"""
        return self.listings
