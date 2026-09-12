from playwright.sync_api import sync_playwright,Page,Locator,FrameLocator
from typing import Union,List

class Actions:
    
    def __init__(self,page:Page):
        self.page=page
        
        
    def _get_locator(self,locator:Union[str,Locator])-> Locator:
        if hasattr(locator,"click") or hasattr(locator,"fill"):
            return locator
        return self.page.locator(locator)
        
        
        
