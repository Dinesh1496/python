# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://dinesh1496.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0DrC1MHA7o7hOcT_zYllI3IVJXZWERcUcVHMvrdF907OnpDh36LJ0KiJ05iv-6aM04sWs-5w5GW0jpvieH0xHMbm0yIwXQn9KLrghfI8yd38ZMikd48HTovr1QdiunECx0xasptbxlrZ7B39ylvz-aOmxDiZm55odoKau78658hs=E849EB94"


auth = HTTPBasicAuth("dinesh1496.kumar@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)


project_name = {output[0]["name"],output[1]["name"]}
project_id = {output[0]["id"],output[1]["id"]}


print(project_name,project_id)