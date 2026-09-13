from playwright.sync_api import sync_playwright,Page,Locator,FrameLocator
from typing import Union,List

class Actions:
    
    def __init__(self,page:Page):
        self.page=page
        
        
    def placeholder(self,text:str):
        return self.page.get_by_placeholder(text)
    
    def role(self, role, **kwargs):
        return self.page.get_by_role(role, **kwargs)
        
    def _get_locator(self,locator:Union[str,Locator])-> Locator:
        if hasattr(locator,"click") or hasattr(locator,"fill"):
            return locator
        return self.page.locator(locator)
    
    def label(self,text: str):
        return self.page.get_by_label(text)
    
    def text_loc(self,text: str):
        return self.page.get_by_text(text)
        
        
        
