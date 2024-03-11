import requests
import json
url = "https://data.mongodb-api.com/app/data-bpgek/endpoint/data/v1/action/find"

payload = json.dumps({
    "collection": "Herbs-Specs",
    "database": "Herbarium",
    "dataSource": "Cluster0"
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'wukJHCAivIHcsAFKMGntRcPEjloYCZAV1m4saVxn6VTECOPl5mxSbbmmIrztgtFy',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
