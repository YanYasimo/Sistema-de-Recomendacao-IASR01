# %%
# get json from a url
import requests
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.16121/dados?formato=json"
response = requests.get(url)
response.json()

# %%
