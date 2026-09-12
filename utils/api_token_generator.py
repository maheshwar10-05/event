from utils.yamlreader import YamlReader


class APILogin:
    def __init__(self,context):
        self.context=context
        
    
    def getToken(self,login_details):
        
        api_response=self.context.post(url="/api/auth/login",data=login_details)
        response_dict=api_response.json()
        response=response_dict.get("token")
        return response
    
    
    
    def event(self, login_details):
        token=self.getToken(login_details)
        event_response = self.context.get(
            url="/api/events?limit=6",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        print("EVENT STATUS:", event_response.status)

        return event_response.json(), event_response.status
            
            