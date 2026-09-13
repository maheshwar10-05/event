from pages.base_page import Basepage


class Homepage(Basepage):
    
    
    def __init__(self, page):
        super().__init__(page)
        
    def event_name(self):
        self.actions.role("link", name="Dilli Diwali Mela").click()
        
    def my_bookings(self):
        self.actions.role("link",name="My Bookings").first.click()
        
    def nav_events(self):
        self.actions.role('link',name='Events').first.click()
        