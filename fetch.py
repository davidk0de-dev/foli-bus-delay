import requests

r = requests.get('http://data.foli.fi/siri/vm')
data = r.json()
# print(data.keys())

print(len(data['result']['vehicles']))