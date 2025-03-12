import unittest
from unittest.mock import Mock
from datetime import datetime
from src.services.user_service import UserService
from src.services.listing_service import ListingService
from src.services.category_service import CategoryService

class TestServices(unittest.TestCase):
    
    def setUp(self):
        # 初始化 Repository
        self.user_repo = Mock()
        self.listing_repo = Mock()
        self.category_repo = Mock()

        # 初始化服務
        self.user_service = UserService(self.user_repo)
        self.category_service = CategoryService(self.category_repo, self.listing_repo, self.user_service)
        self.listing_service = ListingService(self.listing_repo, self.user_service, self.category_service)

        # 對 mock 方法進行 return_value 設置
        self.user_service.validate_user = Mock()
        self.user_repo.user_exists = Mock()
    
    # 測試 UserService
    def test_register_user_success(self):
        # 模擬註冊新用戶
        self.user_repo.user_exists.return_value = False  # 模擬用戶不存在
        result = self.user_service.register("Alice")
        self.assertEqual(result, "Success")  # 預期註冊成功

    def test_register_user_fail(self):
        # 模擬用戶已經存在
        self.user_repo.user_exists.return_value = True  # 模擬用戶已存在
        result = self.user_service.register("Alice")
        self.assertEqual(result, "Error - user already existing")  # 預期返回錯誤訊息

    def test_validate_user(self):
        # 模擬用戶存在
        self.user_repo.user_exists.return_value = True
        result = self.user_service.validate_user("Alice")
        self.assertTrue(result)  # 用戶存在，返回 True
    
    # 測試 ListingService
    def test_create_listing_user_not_found(self):
        # 模擬用戶不存在
        self.user_service.validate_user.return_value = False
        result = self.listing_service.create_listing("nonexistent_user", "Phone", "New model", 800, "Electronics")
        self.assertEqual(result, "Error - user not found")  # 應返回 "Error - user not found"

    def test_get_listing_user_not_found(self):
        # 模擬用戶不存在
        self.user_service.validate_user.return_value = False
        result = self.listing_service.get_listing("nonexistent_user", 100001)
        self.assertEqual(result, "Error - user not found")  # 應返回 "Error - user not found"

    def test_get_listing_not_found(self):
        # 模擬用戶存在，且商品不存在
        self.user_service.validate_user.return_value = True
        self.listing_repo.get_listing.return_value = None  # 模擬商品不存在
        result = self.listing_service.get_listing("Alice", 100001)
        self.assertEqual(result, "Error - not found")  # 應返回 "Error - not found"

    def test_get_listing_success(self):
        # 模擬用戶存在，商品存在
        self.user_service.validate_user.return_value = True
        listing_data = {
            "title": "Phone",
            "description": "New model",
            "price": 800,
            "created_at": "2025-03-12 21:52:20",
            "category": "Electronics",
            "username": "Alice"
        }
        self.listing_repo.get_listing.return_value = listing_data  # 模擬返回商品資料
        result = self.listing_service.get_listing("Alice", 100001)
        self.assertIn("Phone|New model|800", result)  # 應包含商品資訊
    
    
    def test_delete_listing_success(self):
        # 模擬用戶存在且是商品的擁有者
        self.user_service.validate_user.return_value = True
        self.listing_repo.delete_listing.return_value = "Success"  # 模擬刪除成功
        result = self.listing_service.delete_listing("Alice", 100001)
        self.assertEqual(result, "Success")  # 應返回 "Success"
    
    def test_delete_listing_owner_mismatch(self):
        # 模擬用戶不是商品的擁有者
        self.user_service.validate_user.return_value = True
        self.listing_repo.delete_listing.return_value = "Error - listing owner mismatch"  # 模擬錯誤
        result = self.listing_service.delete_listing("Alice", 100001)
        self.assertEqual(result, "Error - listing owner mismatch")  # 應返回錯誤訊息

    # 測試 CategoryService
    def test_get_category_listings_user_not_found(self):
        # 模擬用戶不存在
        self.user_service.validate_user.return_value = False
        result = self.category_service.get_category_listings("nonexistent_user", "Electronics")
        self.assertEqual(result, "Error - user not found")  # 應返回錯誤訊息

    def test_get_category_listings_success(self):
        # 模擬用戶存在，且分類有商品
        self.user_service.validate_user.return_value = True
        self.category_repo.get_category_listings.return_value = [100001, 100002]  # 模擬返回商品 ID
        self.listing_repo.get_listing.side_effect = [
            {"title": "Phone", "description": "New model", "price": 800, "created_at": "2025-03-12 21:52:20", "category": "Electronics", "username": "Alice"},
            {"title": "Laptop", "description": "Gaming laptop", "price": 2500, "created_at": "2025-03-12 21:52:21", "category": "Electronics", "username": "Alice"}
        ]
        result = self.category_service.get_category_listings("Alice", "Electronics")
        self.assertIn("Phone|New model|800", result)
        self.assertIn("Laptop|Gaming laptop|2500", result)

    def test_get_top_category_user_not_found(self):
        # 模擬用戶不存在
        self.user_service.validate_user.return_value = False
        result = self.category_service.get_top_category("nonexistent_user")
        self.assertEqual(result, "Error - user not found")  # 應返回錯誤訊息

    def test_get_top_category_success(self):
        # 模擬用戶存在且返回最熱門的分類
        self.user_service.validate_user.return_value = True
        self.category_repo.get_top_category.return_value = "Electronics"  # 模擬返回熱門分類
        result = self.category_service.get_top_category("Alice")
        self.assertEqual(result, "Electronics")  # 應返回 "Electronics"
    

if __name__ == "__main__":
    unittest.main()