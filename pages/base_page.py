from utils.actions import Actions
from utils.env_reader import EnvReader
from utils.yamlreader import YamlReader
from pages.APIlogin import APILogin
import json
login_details=YamlReader.read_yaml(filename="login_details.yaml", folder="testdata")
class Basepage:
    
    def __init__(self,page):
        self.page=page
        self.actions=Actions(page)
        self.config=EnvReader.get_env_config()
        
        
    def inject(self, api_context):

        api_login = APILogin(api_context)

        token = api_login.getToken(login_details)

        print("API TOKEN:", token)

        assert token is not None, "Token was not generated"

        self.page.add_init_script(
            f"""
            localStorage.setItem('token', '{json.dumps(token)}');
            """
        )    
        
    def open(self):
        self.page.goto(self.config["base_url"])
        
                
    
 
        
    