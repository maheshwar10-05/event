from pages.register_page import Register
from pages.login_page import Login
from utils.yamlreader import YamlReader
import time
reg_details= YamlReader.read_yaml(filename="registerdetails.yaml",folder="testdata")

def test_register(page):
    reg_obj=Register(page)
    log_obj=Login(page)
    log_obj.open()
    log_obj.reg_button()
    reg_obj.enter_email(reg_details["email"])
    reg_obj.enter_password(reg_details["password"])
    reg_obj.confirm(reg_details["repeat_pass"])
    reg_obj.click_create()
    pass
    

