from utils.yamlreader import YamlReader
from pages.APIlogin import APILogin


login_details=YamlReader.read_yaml(filename="login_details.yaml", folder="testdata")

def test_event_details(api_context):
    api_obj=APILogin(api_context)
    response,status=api_obj.event(login_details)
    print(response,status)