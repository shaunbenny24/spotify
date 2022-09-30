import requests
from urllib.parse import urlencode
import base64
import webbrowser



client_id = "3ff8c0cee40a48b78dfaf3820dca8969"
client_secret = "9173685928a44ff29dd00e2c2fdfedb9"

# auth_headers = {
#     "client_id": client_id,
#     "response_type": "code",
#     "redirect_uri": "http://localhost:7777/callback",
#     "scope": "user-library-read"
# }

# webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))


code="AQBIGly0mFjmizYNpTOs83_bQAEAZH9dFK2xacKfljIHCK86nUyjPD-ijN25Vqkxteheo--zQ75xilCly0pQbLHLu1exOmZsHYi0WWfAey_OzToYu2FOK2SUuGC80EeNM1JG5SDSU48PR4OXQ5NV9bODZVFLgePKUh4NPUzRXOzzpVZGRJpiGwCDXcnLw4fMzfPh-ug"

encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:7777/callback"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

token = r.json()


print(token)


# token = 'BQBwitnQzEPRY4KSId_YRVxXUnET9Pvz0e6TlV5HbY67dtO_Cdq3CYK-rxQzas2cdBRuYaqXzc80TF2Ro-8IA0hoK4E2I4PRfix2CGkqDrEPc04P8LOHO1LRp_wl2apOsUryofEGkeE9zSwKiIwHlx4_lpcos4NVljx6hb_Kph-gwDWaF-R9hWZdDg05-8e1e_1Me-bnQ49FV4Yp47k'


# user_headers = {
#     "Authorization": "Bearer " + token,
#     "Content-Type": "application/json"
# }

# user_params = {
#     "limit": 50
# }

# user_tracks_response = requests.get('https://api.spotify.com/v1/search?q=anirudh&type=artist', params=user_params, headers=user_headers)

# print(user_tracks_response.json())