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

    def remove_listing_from_category(self, category, listing_id):
        """移除商品分類"""
        if category not in self.categories:
            return "Error - category not found"

        for i, (lid, _) in enumerate(self.categories[category]):
            if lid == listing_id:
                del self.categories[category][i]
                if not self.categories[category]:
                    del self.categories[category]
                return "Success"
        return "Error - listing not found in category"

    def get_category_listings(self, category):
        """獲取分類內的所有商品 ID，依建立時間排序"""
        if category not in self.categories:
            return "Error - category not found"
        return [listing[0] for listing in self.categories[category]]

    def get_top_category(self):
        """獲取擁有最多商品的分類"""
        if not self.categories:
            return []

        # 計算每個分類的商品數量
        category_counts = {category: len(listings) for category, listings in self.categories.items()}

        # 找到擁有最多商品數量的分類
        max_count = max(category_counts.values())

        # 找出所有擁有最多商品的分類
        top_categories = [category for category, count in category_counts.items() if count == max_count]

        # 如果有多個分類擁有最多商品，按字典順序排序
        top_categories.sort()

        return top_categories
