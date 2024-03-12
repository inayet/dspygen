import requests
import json

# mock api endpoints for passing in code to get access,refresh tokens
url = "https://stoplight.io/mocks/highlevel/integrations/39582851/oauth/token"

payload='client_id=21323897adaad32546874987&client_secret=0546a54dad8f7a3654a35fd4&grant_type=authorization_code&code=87956465487987654654dafde&user_type=Company&redirect_uri=https://localhost:8501/redircting' 
headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

response = requests.request("POST", url, headers=headers, data=payload)

# tried not to use json to access refresh token but was forced to, will try alternative methods
refresh_token = json.loads(response.__dict__['_content'].decode('utf-8'))['refresh_token']
print(refresh_token)

