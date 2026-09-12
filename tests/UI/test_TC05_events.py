from pages.eventspage import Events

from pages.bookings_page import Bookings
from pages.base_page import Basepage
from pages.login_page import Login
from pages.homepage import Homepage
from pages.APIlogin import APILogin
from utils.yamlreader import YamlReader
login_details=YamlReader.read_yaml(filename="login_details.yaml", folder="testdata")


def test_event_cities(page):
    event_obj=Events(page)
    base_page = Basepage(page)
    login_obj=Login(page)
    base_page.open()
        
    login_obj.enter_username(login_details['email'])
    login_obj.password(login_details['password'])
    login_obj.signin_button()
    home_page = Homepage(page)
    home_page.nav_events()
    event_obj.event_cities()
    
    