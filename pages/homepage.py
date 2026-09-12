from pages.base_page import Basepage


class Homepage(Basepage):
    
    event1="a[href='/events/3']"
    
    def __init__(self, page):
        super().__init__(page)
        
    def event_name(self):
        self.page.get_by_role("link", name="Dilli Diwali Mela").click()
        
    def my_bookings(self):
        self.page.get_by_role("link",name="My Bookings").first.click()
        
    def nav_events(self):
        self.page.get_by_role('link',name='Events').first.click()
        