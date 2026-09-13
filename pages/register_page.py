from pages.base_page import Basepage

class Register(Basepage):
    email_loc="you@email.com"
    password_loc="Min 8 chars, uppercase, number & symbol"
    confirm_password="Repeat your password"
    error_locator="p[class='mt-1 text-xs text-red-600']"
    
    def __init__(self, page):
        super().__init__(page)
        
    def enter_email(self,email):
        self.actions.placeholder(self.email_loc).fill(email)
    def enter_password(self,password):
        self.actions.placeholder(self.password_loc).fill(password)
    def confirm(self,password):
        self.actions.placeholder(self.confirm_password).fill(password)
        
    def click_create(self):
        self.actions.role("button",name="Create Account").click()
    def error_message(self):
        error=self.page.locator(self.error_locator).text_content().strip()
        return error
        
    