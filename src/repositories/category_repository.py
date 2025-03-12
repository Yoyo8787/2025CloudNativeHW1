class CategoryRepository:
    def __init__(self):
        """初始化分類儲存"""
        self.categories = {}

    def add_listing_to_category(self, category, listing_id, created_at):
        """將商品加入分類（若分類不存在則自動建立）"""
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append((listing_id, created_at))

        # 依照 created_at 進行排序 (新商品在最前面)
        self.categories[category].sort(key=lambda x: x[1], reverse=True)

    def get_category_listings(self, category):
        """獲取分類內的所有商品 ID，依建立時間排序"""
        if category not in self.categories:
            return "Error - category not found"
        return [listing[0] for listing in self.categories[category]]

    def get_top_category(self):
        """獲取擁有最多商品的分類"""
        if not self.categories:
            return None
        return max(self.categories, key=lambda cat: len(self.categories[cat]))
