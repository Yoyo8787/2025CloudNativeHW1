import unittest
from unittest.mock import Mock
from src.controllers.user_controller import UserController
from src.controllers.listing_controller import ListingController
from src.controllers.category_controller import CategoryController
from src.services.user_service import UserService
from src.services.listing_service import ListingService
from src.services.category_service import CategoryService


class TestControllers(unittest.TestCase):

    def setUp(self):
        # 初始化 Mock 服務
        self.user_service = Mock(spec=UserService)
        self.listing_service = Mock(spec=ListingService)
        self.category_service = Mock(spec=CategoryService)

        # 初始化控制器
        self.user_controller = UserController(self.user_service)
        self.listing_controller = ListingController(self.listing_service)
        self.category_controller = CategoryController(self.category_service)
    
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"Controller test passed: {test._testMethodName}")

    # 測試 UserController
    def test_register_user_success(self):
        # 模擬註冊成功
        self.user_service.register.return_value = "Success"
        result = self.user_controller.register("Alice")
        self.assertEqual(result, "Success")
        self.user_service.register.assert_called_with("Alice")  # 確保註冊方法被正確調用

    def test_register_user_fail(self):
        # 模擬用戶已存在
        self.user_service.register.return_value = "Error - user already existing"
        result = self.user_controller.register("Alice")
        self.assertEqual(result, "Error - user already existing")
        self.user_service.register.assert_called_with("Alice")

    # 測試 ListingController
    def test_create_listing(self):
        # 模擬商品創建成功
        self.listing_service.create_listing.return_value = "100001"
        result = self.listing_controller.create_listing("Alice", "Phone", "New model", 800, "Electronics")
        self.assertEqual(result, "100001")
        self.listing_service.create_listing.assert_called_with("Alice", "Phone", "New model", 800, "Electronics")

    def test_get_listing(self):
        # 模擬商品查詢成功
        listing_data = {"title": "Phone", "description": "New model", "price": 800}
        self.listing_service.get_listing.return_value = listing_data
        result = self.listing_controller.get_listing("Alice", 100001)
        self.assertEqual(result, listing_data)
        self.listing_service.get_listing.assert_called_with("Alice", 100001)

    def test_delete_listing(self):
        # 模擬商品刪除成功
        self.listing_service.delete_listing.return_value = "Success"
        result = self.listing_controller.delete_listing("Alice", 100001)
        self.assertEqual(result, "Success")
        self.listing_service.delete_listing.assert_called_with("Alice", 100001)

    # 測試 CategoryController
    def test_get_category(self):
        # 模擬查詢分類商品成功
        self.category_service.get_category_listings.return_value = "Phone|New model|800"
        result = self.category_controller.get_category("Alice", "Electronics")
        self.assertEqual(result, "Phone|New model|800")
        self.category_service.get_category_listings.assert_called_with("Alice", "Electronics")

    def test_get_top_category(self):
        # 模擬查詢最熱門分類成功
        self.category_service.get_top_category.return_value = "Electronics"
        result = self.category_controller.get_top_category("Alice")
        self.assertEqual(result, "Electronics")
        self.category_service.get_top_category.assert_called_with("Alice")


if __name__ == "__main__":
    unittest.main()
