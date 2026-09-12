from pages.base_page import Basepage
from utils.actions import Actions
import pytest


class Login(Basepage):
    
    user_name="you@email.com"
    password_enter="••••••"
    register_link="Register"
    def __init__(self, page):
        super().__init__(page)
    def enter_username(self,username):
        self.page.get_by_placeholder(self.user_name).fill(username)
    def password(self,password):
        self.page.get_by_placeholder(self.password_enter).fill(password)
    def signin_button(self):
        self.page.get_by_role("button",name="Sign In").click()
    #def reg_button(self):
        #self.page.get_by_text(self.register_link).click()