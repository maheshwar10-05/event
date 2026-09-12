from pages.APIlogin import APILogin
from utils.yamlreader import YamlReader
from pages.homepage import Homepage
from pages.base_page import Basepage
from pages.login_page import Login
import time
login_details=YamlReader.read_yaml(filename="login_details.yaml", folder="testdata")

def test_event(api_context,page):
    base_page = Basepage(page)
    login_obj=Login(page)
    base_page.inject(api_context)
    
    base_page.open()
    
    login_obj.enter_username(login_details['email'])
    login_obj.password(login_details['password'])
    login_obj.signin_button()
    home_page = Homepage(page)
    home_page.event_name()
    time.sleep(2)
    
def test_nav_my_bookings(page):
    base_page = Basepage(page)
    login_obj=Login(page)
    base_page.open()
        
    login_obj.enter_username(login_details['email'])
    login_obj.password(login_details['password'])
    login_obj.signin_button()
    home_page = Homepage(page)
    home_page.my_bookings()
  
    
    
    
    
    