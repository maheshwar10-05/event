from pages.base_page import Basepage
from utils.actions import Actions

class Bookings(Basepage):
    booking_id_loc="#booking-id"
    
    def __init__(self, page):
        super().__init__(page)
        
    def confirmed_bookings(self):
        
        b_id=self.page.locator(self.booking_id_loc).text_content().strip()
        cleaned_id=b_id.replace("#","")
        print(f"Booking id from UI is {cleaned_id}")
        return cleaned_id
        
        
    