from pages.base_page import Basepage
import openpyxl

class Events(Basepage):
    event_cities_loc="//div[@class='flex flex-col gap-1 sm:w-40']/select"
    
    def __init__(self, page):
        super().__init__(page)
        
    def event_cities(self):
        cities=self.page.locator(self.event_cities_loc).all_inner_texts()
        for city in cities:
            if '\n' in city:
                new_city=city.replace('\n'," ")
            else:
                print(new_city,end=" ")
            
         
        
        
    