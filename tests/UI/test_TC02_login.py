from pages.login_page import Login
from utils.yamlreader import YamlReader
import time,pytest
login_details= YamlReader.read_yaml(filename="login_details.yaml",folder="testdata")


def test_login(page):
    log_obj=Login(page)
    log_obj.open()
    log_obj.enter_username(login_details["email"])
    log_obj.password(login_details["password"])
    log_obj.signin_button()
    