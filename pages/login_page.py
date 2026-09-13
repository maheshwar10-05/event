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
        self.actions.placeholder(self.user_name).fill(username)
    def password(self,password):
        self.actions.placeholder(self.password_enter).fill(password)
    def signin_button(self):
        self.actions.role("button",name="Sign In").click()
    def reg_button(self):
        self.actions.text_loc(self.register_link).click()