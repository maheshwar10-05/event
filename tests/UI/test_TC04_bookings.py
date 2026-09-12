from pages.bookings_page import Bookings
from pages.base_page import Basepage
from pages.login_page import Login
from pages.homepage import Homepage
from pages.APIlogin import APILogin
from utils.yamlreader import YamlReader
login_details=YamlReader.read_yaml(filename="login_details.yaml", folder="testdata")

def test_booking_id(api_context,page):
    api_obj=APILogin(api_context)
    book_obj=Bookings(page)
    base_page = Basepage(page)
    login_obj=Login(page)
    base_page.open()
        
    login_obj.enter_username(login_details['email'])
    login_obj.password(login_details['password'])
    login_obj.signin_button()
    home_page = Homepage(page)
    home_page.my_bookings()
    booking_id_ui=book_obj.confirmed_bookings()
    booking_id_api=api_obj.getBookingid(login_details)
    assert int(booking_id_ui)==booking_id_api
    
    