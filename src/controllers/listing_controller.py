
class ListingController:
    def __init__(self, listing_service):
        self.listing_service = listing_service

    def create_listing(self, username, title, description, price, category):
        return self.listing_service.create_listing(username, title, description, price, category)

    def get_listing(self, username, listing_id):
        return self.listing_service.get_listing(username, listing_id)

    def delete_listing(self, username, listing_id):
        return self.listing_service.delete_listing(username, listing_id)
