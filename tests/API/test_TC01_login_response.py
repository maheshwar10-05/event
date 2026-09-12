from utils.yamlreader import YamlReader
from pages.APIlogin import APILogin


login_details=YamlReader.read_yaml(filename="login_details.yaml", folder="testdata")

def test_api_login(api_context):
    api_obj=APILogin(api_context)
    data=api_obj.getToken(login_details)
    print(data,end="")
    

    
    
    