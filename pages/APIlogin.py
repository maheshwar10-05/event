import json,copy
class APILogin:
    def __init__(self,context):
        self.context=context
        
    
    def getToken(self,login_details):
        
        api_response=self.context.post(url="/api/auth/login",data=login_details)
        response_dict=api_response.json()
        response_str=json.dumps(response_dict,indent=4)
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
    
    
    def getBookingid(self,login_details):
        token=self.getToken(login_details)
        booking_info=self.context.get(url='/api/bookings?page=1&limit=10',headers={"Authorization": f"Bearer {token}"})
        booking_dict=booking_info.json()
        for data in booking_dict['data']:
            if isinstance(data,dict):
                booking_id=data.get('id')
        print(f' booking ID from API is {booking_id}')
        return booking_id 
        
        
        
            
            