import unittest
from src.repositories.user_repository import UserRepository
from src.repositories.listing_repository import ListingRepository
from src.repositories.category_repository import CategoryRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        """在每個測試執行前初始化 UserRepository"""
        self.user_repo = UserRepository()

    def test_add_user(self):
        self.user_repo.add_user("Alice")
        self.assertTrue(self.user_repo.user_exists("alice"))
        self.assertTrue(self.user_repo.user_exists("Alice"))
        self.assertFalse(self.user_repo.user_exists("Bob"))

    def test_case_insensitive(self):
        self.user_repo.add_user("TestUser")
        self.assertTrue(self.user_repo.user_exists("testuser"))
        self.assertTrue(self.user_repo.user_exists("TESTUSER"))

class TestListingRepository(unittest.TestCase):
    def setUp(self):
        self.listing_repo = ListingRepository()

    def test_add_listing(self):
        listing_id = self.listing_repo.add_listing("Alice", "Laptop", "Brand new", 1000, "Electronics")
        listing = self.listing_repo.get_listing(listing_id)
        self.assertIsNotNone(listing)
        self.assertEqual(listing["title"], "Laptop")
        self.assertEqual(listing["price"], 1000)

    def test_delete_listing(self):
        listing_id = self.listing_repo.add_listing("Alice", "Laptop", "Brand new", 1000, "Electronics")
        self.assertEqual(self.listing_repo.delete_listing("Bob", listing_id), "Error - listing owner mismatch")
        self.assertEqual(self.listing_repo.delete_listing("Alice", listing_id), "Success")
        self.assertIsNone(self.listing_repo.get_listing(listing_id))

class TestCategoryRepository(unittest.TestCase):
    def setUp(self):
        self.category_repo = CategoryRepository()

    def test_add_listing_to_category(self):
        self.category_repo.add_listing_to_category("Electronics", 100001, "2025-03-12 14:00:00")
        self.category_repo.add_listing_to_category("Electronics", 100002, "2025-03-12 15:00:00")
        listings = self.category_repo.get_category_listings("Electronics")
        self.assertEqual(listings, [100002, 100001])

    def test_get_top_category(self):
        self.category_repo.add_listing_to_category("Electronics", 100001, "2025-03-12 14:00:00")
        self.category_repo.add_listing_to_category("Sports", 100002, "2025-03-12 15:00:00")
        self.category_repo.add_listing_to_category("Sports", 100003, "2025-03-12 16:00:00")
        self.assertEqual(self.category_repo.get_top_category(), ['Sports'])



if __name__ == '__main__':
    unittest.main()
